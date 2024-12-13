"""Task Configuration


"""
from litestash.core.config.root import Valid
from litestash.core.config.litestash_conf import EngineAttr
from litestash.core.config.litestash_conf import SessionAttr


class TaskSlots(Valid):
    """The attribute Slots for a Task thread."""
    DB_NAME = f'{EngineAttr.DB_NAME.value}'
    SESSION = f'{SessionAttr.SESSION.value}'
    LOCK = 'lock'

    @staticmethod
    def slots():
        """Get the slots for a Task"""
        return tuple([slot.value for slot in TaskSlots])


class TaskAttr(Valid):
    """The namedtuple config for all task attributes of a LiteStash"""
    TYPE_NAME = 'TaskAttributes'
    DB_NAME = f'{EngineAttr.DB_NAME.value}'
    TASK = 'task'
    VALUE_ERROR = 'todo'
    DOC = '''
        A namedtuple representing task attributes for a specific database:

            - db_name (str): The name of the database.
            - task (Task): The Task instance associated with this database.

        This structure helps in managing tasks alongside their respective
        databases.
    '''
