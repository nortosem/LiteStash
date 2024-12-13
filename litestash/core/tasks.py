"""LiteStash Task Manager

Creates and provides access to task facotories for each database in LiteStash.
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
        self.tables_03 = setup_tasks(session.get(Tables.TABLES_03.value))
        self.tables_47 = setup_tasks(session.get(Tables.TABLES_47.value))
        self.tables_89hu = setup_tasks(session.get(Tables.TABLES_89HU.value))
        self.tables_ab = setup_tasks(session.get(Tables.TABLES_AB.value))
        self.tables_cd = setup_tasks(session.get(Tables.TABLES_CD.value))
        self.tables_ef = setup_tasks(session.get(Tables.TABLES_EF.value))
        self.tables_gh = setup_tasks(session.get(Tables.TABLES_GH.value))
        self.tables_ij = setup_tasks(session.get(Tables.TABLES_IJ.value))
        self.tables_kl = setup_tasks(session.get(Tables.TABLES_KL.value))
        self.tables_mn = setup_tasks(session.get(Tables.TABLES_MN.value))
        self.tables_op = setup_tasks(session.get(Tables.TABLES_OP.value))
        self.tables_qr = setup_tasks(session.get(Tables.TABLES_QR.value))
        self.tables_st = setup_tasks(session.get(Tables.TABLES_ST.value))
        self.tables_uv = setup_tasks(session.get(Tables.TABLES_UV.value))
        self.tables_wx = setup_tasks(session.get(Tables.TABLES_WX.value))
        self.tables_yz = setup_tasks(session.get(Tables.TABLES_YZ.value))


    def get(self, db_name):
        """Gets the task for the specified database.

        Args:
            db_name (str): The name of the datase (e.g. "tables_03").

        Returns:
            task (Task): The task queue that manages workers for that database.

        Raises:
            AttributeError:
        """
        attribute = getattr(self, db_name)
        return attribute.task


    def __iter__(self):
        """Yields all Tasks attributres"""
        yield from (getattr(self, slot) for slot in self.__slots__)


    def __repr__(self):
        """todo"""
        pass


    def __str__(self):
        """todo"""
        pass
