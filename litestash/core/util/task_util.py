"""Task Utility Module

This module provides utilities for managing asynchronous tasks related to
SQLite database operations within the LiteStash system. It uses asyncio
for handling concurrent database access across different threads.

Functions:

- `setup_tasks`:
  Creates and returns a `TaskAttributes` namedtuple containing a task
  instance for a specific database.

Classes:

- `Task`: Manages the execution of database operations in an asynchronous,
  thread-safe manner for each database.
"""
import asyncio
from asyncio import Lock
from asyncio import Future
from typing import Any
from typing import Tuple
from typing import Callable
from pydantic import StrictBool
from collections import namedtuple
from litestash.models import LiteStashData
from litestash.logging import root_logger as logger
from litestash.core.config.task_conf import TaskAttr
from litestash.core.config.task_conf import TaskSlots
from litestash.core.util.core_util import SessionAttributes


class Task:
    """Task

    This class manages the creation and access to task runners for each
    SQLite database, ensuring thread-safe operations using asyncio.

    Attributes:
        db_name (str): The name of the database this task is associated with.
        session (Session): The session object for database operations.
        lock (Lock): An asyncio lock for managing concurrent access.
        loop (asyncio.AbstractEventLoop): The event loop for scheduling tasks.

    Methods:
        __run: Private async method to run tasks in a thread-safe manner.
        send: Public method to schedule tasks in the event loop.
    """
    __slots__ = TaskSlots.slots()

    def __init__(self,
        session: SessionAttributes,
        new_loop: StrictBool = False
    ):
        """Task Constructor

        Initialize the thread Task and link it to a database.

        Args:
            session (SessionAttributes): Session attributes for database
                interaction.
            new_loop (StrictBool): If True, creates a new event loop;
                otherwise, uses the running one.
        """
        self.db_name = session.db_name
        self.session = session.session
        self.lock = Lock()

        def _mk_loop(self):
            self.loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self.loop)

        if not new_loop:
            try:
                self.loop = asyncio.get_running_loop()
            except RuntimeError:
                logger.warning('No running event loop found; creating new one.')
                _mk_loop(self)
        else:
            _mk_loop(self)


    async def __run(self, work: Tuple[Callable, LiteStashData]) -> Any:
        """Run

        The Task thread work function processor. Execute the api function in a
        thread-safe manner.

        Args:
            work (Tuple): A tuple containing the api function used to process
                LiteStash data.

        Returns:
            result (Any): The result of the function execution.

        Raises:
            Exception: Log and raise any errors during task execution.
        """
        try:
            async with self.lock:
                func, data = work
                result = await asyncio.to_thread(func, data)
                return result
        except Exception as unknown_error:
            logger.error('Task for %s raised error: %s',
                func.__name__, unknown_error)
            raise


    def send(self, func: Callable, data: LiteStashData) -> Future:
        """Send

        Schedule a job for the task to run in the context of its database's
        event loop.

        Args:
            func (Callable): The function to call, expecting LiteStashData as an
                argument.
            data (LiteStashData): The LiteStash data (key and/or value) to
                process.

        Returns:
            Future: A future representing the result of the task.
        """
        work = (func, data)
        future = asyncio.run_coroutine_threadsafe(
            self.__run(work), self.loop
        )
        return future


TaskAttributes = namedtuple(
    TaskAttr.TYPE_NAME.value,
    [
        TaskAttr.DB_NAME.value,
        TaskAttr.TASK.value
    ]
)
TaskAttributes.__doc__ = TaskAttr.DOC.value


def setup_tasks(session: SessionAttributes) -> TaskAttributes:
    """Creates and returns TaskAttributes for a specific database.

    This function initializes a Task for the given session, encapsulating
    database-specific task management.

    Args:
        session (SessionAttributes): The session attributes for the database
            to set up.

    Returns:
        TaskAttributes: A namedtuple containing the database name and
            the corresponding Task instance.

    """
    task = Task(session)
    task = TaskAttributes(session.db_name, task)
    return task
