"""Task Configuration


"""
from litestash.core.config.root import Valid
from litestash.core.config.litestash_util import EngineAttr
from litestash.core.config.litestash_util import SessionAttr

class TaskConf(Valid):
    """The Configuration valudes for a Task"""
    MAX_QUEUE = 8


class TaskSlots(Valid):
    """The attribute Slots for a Task thread."""
    DB_NAME = f'{EngineAttr.DB_NAME.value}'
    SESSION = f'{SessionAttr.SESSION.value}'
    QUEUE = 'queue'
    LOCK = 'lock'

    @staticmethod
    def get():
        """Get the slots for a Task"""
        return tuple([slot.value for slot in TaskSlots])


class TaskAttr(Valid):
    """The namedtuple config for all task attributes of a LiteStash"""
    TYPE_NAME = 'TaskAttributes'
    DB_NAME = f'{EngineAttr.DB_NAME.value}'
    TASK = 'task'
    VALUE_ERROR = 'todo'
    DOC = '''todo'''
