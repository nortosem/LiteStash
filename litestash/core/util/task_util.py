"""Task Utility Module

The task module defines the utility functions for managing threads with the
sqlite database files for LiteStash.

Functions:

- `create_task`:
- `setup_tasks`:

"""
from queue import Queue
from typing import Callable
from threading import Lock
from threading import Thread
from collections import namedtuple
from litestash.models import LiteStashData
from litestash.logging import root_logger as logger
from litestash.core.config.task_conf import TaskConf
from litestash.core.config.task_conf import TaskAttr
from litestash.core.config.task_conf import TaskSlots
from litestash.core.util.core_util import SessionAttributes


class Task:
    """Task

    This class manages the creation and access to task runners for each
    database thread.

    Attributes:

        db_name (str):
        session (Session):
        queue (Queue):
        thread (Tread):
        lock (Lock):

    Methods:
        __run:
        send:
        stop:
    """
    __slots__ = TaskSlots.get()

    def __init__(self, session: SessionAttributes):
        """Task Constructor

        Initialize the thread Task and link it to a database.
        """
        self.db_name = session.db_name
        self.session = session.session
        self.queue = Queue(maxsize=TaskConf.MAX_QUEUE.value)
        self.thread = Thread(target=self.__run)
        self.thread.daemon = True
        self.thread.start()
        self.lock = Lock()


    def __run(self):
        """Run

        The Task thread's internal work function processor
        """
        while True:
            work = self.queue.get()
            if work is None:
                break
            try:
                with self.lock:
                    func, data, future = work
                    result = func(data)
                    future.set_result(result)
            except Exception as unknown_error:
                future.set_exception(unknown_error)
                logger.error('Task for %s raised error: %s',
                    func.__name__, unknown_error)
                raise
            finally:
                self.queue.task_done()


    def send(self, func: Callable, data: LiteStashData, future=None):
        """Send

        Send a job for the task to run in the queue for its database.

        Args:
            func (Callable): The API function to call
            data (LiteStashData): The given key and, or, value.
                future (Future): The Future object for this task.
        """
        self.queue.put((func, data, future))


    def stop(self):
        """Stop
        Top the thread for this database.
        """
        self.queue.put(None)
        self.queue.join()


def setup_tasks(session: SessionAttributes) -> TaskAttributes:
    """Creates and returns Task and returns it for a specific database.

    Args:

        db_name (StrictStr): Name of of the database being threaded

    Returns:

        TaskAttribute:

    Raises:

    """
    task = Task(session)
    task = TaskAttributes(session.db_name, task)
    return task


TaskAttributes = namedtuple(
    TaskAttr.TYPE_NAME.value,
    [
        TaskAttr.DB_NAME.value,
        TaskAttr.TASK.value
    ]
)
TaskAttributes.__doc__ = TaskAttr.DOC.value
