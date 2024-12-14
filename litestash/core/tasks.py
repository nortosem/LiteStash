"""LiteStash Task Manager

Manages the creation and access to task threads for each database in LiteStash,
facilitating concurrent operations across multiple SQLite databases.
"""
from litestash.core.config.root import Tables
from litestash.core.util.task_util import setup_tasks
from litestash.core.util.core_util import SessionAttributes


class Tasks:
    """LiteStash Tasks

    Args:
        session (SessionStash): Impore the core.session.Session container
            and use the sessiont to generate Task threads for each database.
    """
    __slots__ = Tables.slots()

    def __init__(self, session: SessionAttributes):
        """Task Constructor

        Initialize the thread Task and link it to a database.
        """
        for table in self.__slots__:
            setattr(self, table, setup_tasks(session.get(table)))


    def get(self, db_name):
        """Gets the task for the specified database.

        Args:
            db_name (str): The name of the datase (e.g. "tables_03").

        Returns:
            task (Task): The task queue that manages workers for that database.

        Raises:
            AttributeError:
        """
        attribute = getattr(self, db_name, None)
        if attribute is None:
            raise AttributeError(f'Datbase {db_name} not found')
        return attribute.task


    def __iter__(self):
        """Yields all Tasks attributres"""
        yield from (getattr(self, slot) for slot in self.__slots__)


    def __repr__(self):
        """Representation of Tasks

        Provides a string representation of the Tasks instance.

        Returns:
            str: A string describing the Tasks instance.
        """
        return f"Tasks({', '.join(self.__slots__)})"

    def __str__(self):
        """String of Tasks

        Gives a concise string of the Tasks instance.

        Returns:
            str: A string with the number of managed databases.
        """
        return f"Tasks(databases={len(self.__slots__)})"
