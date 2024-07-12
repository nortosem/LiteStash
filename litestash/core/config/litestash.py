"""The LiteStash Attribue Module

#TODO doc
"""

class EngineAttr(Valid):
    """The namedtuple config for all engine attributes of a LiteStash"""
    TYPE_NAME = 'StashEngine'
    DB_NAME = 'db_name'
    ENGINE = 'engine'
    DOC = '''Defines a named tuple for tuple returned by utils.setup_engine.
    Attributes:
        db_name (str): name of the database for this engine
        engine (Engine): the sqlalchemy engine itself
    '''
    VALUE_ERROR = 'No such engine found'


class MetaAttr(Valid):
    """The namedtuple config for all metadata attributes of a LiteStash"""
    TYPE_NAME = 'StashMeta'
    DB_NAME = f'{EngineStash.DB_NAME.value}'
    METADATA = 'metadata'
    DOC = '''todo'''

class SessionAttr(Valid):
    """The namedtuple config for all session attribues of a LiteStash """
    TYPE_NAME = 'StashSession'
    DB_NAME = f'{EngineStash.DB_NAME.value}'
    SESSION = 'session'
    VALUE_ERROR = 'Invalid database: no tables found'
    DOC = '''todo'''
