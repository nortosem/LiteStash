import pytest
from pathlib import Path
from tests.core.config.test_root import name_chk, value_chk
from litestash.core.config.litestash_conf import (
    Key, MkHash, DigestKey, StashError, DataScheme, StashSlots,
    Utils, EngineAttr, MetaAttr, SessionAttr, EngineConf
)

def test_key():
    assert 'LOG_ERROR' == Key.LOG_ERROR.name
    assert 'TYPE_ERROR' ==  Key.TYPE_ERROR.name
    assert 'Expected a string, but got incorrect type: ' == Key.LOG_ERROR.value
    assert 'Key must be a string' == Key.TYPE_ERROR.value
    assert Key.log_error() == 'Expected a string, but got incorrect type: '
    assert Key.type_error() == 'Key must be a string'


def test_mkhash():
    assert 'NONE_LOG' in name_chk(MkHash) #== MkHash.NONE_LOG.name
    assert 'VALUE_ERROR' in name_chk(MkHash)  #MkHash.VALUE_ERROR.name
    assert 'BYTES_LOG' in name_chk(MkHash) #MkHash.BYTES_LOG.name
    assert 'BYTES_ERROR' in name_chk(MkHash) #MkHash.BYTES_ERROR.name
    assert 'DIGEST_LOG' in name_chk(MkHash) #MkHash.DIGEST_LOG.name
    assert '' in value_chk(MkHash)


def test_digestkey():
    assert 'DIGEST_KEY_LOG' in name_chk(DigestKey) #DigestKey.DIGEST_KEY_LOG.name
    assert 'DIGEST_KEY_ERROR' in name_chk(DigestKey) #DigestKey.DIGEST_KEY_ERROR.name
    assert '' in value_chk(DigestKey)


def test_stasherror():
    assert 'SET_TYPE' == StashError.SET_TYPE.name
    assert 'KEY_TYPE' == StashError.KEY_TYPE.name
    assert 'value must be JSON serializable' == StashError.SET_TYPE.value
    assert 'Key must be a string' == StashError.KEY_TYPE.value


def test_data_scheme():
    assert 'TITLE' == DataScheme.TITLE.name
    assert 'DESCRIPTION' == DataScheme.DESCRIPTION.name
    assert 'MIN_LENGTH' == DataScheme.MIN_LENGTH.name
    assert 'MAX_LENGTH' == DataScheme.MAX_LENGTH.name
    assert 'FORBID_EXTRA' == DataScheme.FORBID_EXTRA.name
    assert 'FROM_ATTRIBUTES' == DataScheme.FROM_ATTRIBUTES.name
    assert 'Data' == DataScheme.TITLE.value
    assert 'The key name and JSON data for the given key.' == DataScheme.DESCRIPTION.value
    assert 3 == DataScheme.MIN_LENGTH.value
    assert 999 == DataScheme.MAX_LENGTH.value
    assert 'forbid' == DataScheme.FORBID_EXTRA.value
    assert False == DataScheme.FROM_ATTRIBUTES.value

def test_stash_slots():
    assert StashSlots.ENGINE.name == 'ENGINE'
    assert StashSlots.METADATA.name == 'METADATA'
    assert StashSlots.DB_SESSION.name == 'DB_SESSION'
    assert StashSlots.ENGINE.value == 'engine'
    assert StashSlots.METADATA.value == 'metadata'
    assert StashSlots.DB_SESSION.value == 'db_session'
    assert StashSlots.slots() == ('engine', 'metadata', 'db_session')

def test_utils():
    assert Utils.SIZE.name == 'SIZE'
    assert Utils.DB_NAME_ERROR.name == 'DB_NAME_ERROR'
    assert Utils.INVALID_CHAR_LENGTH.name == 'INVALID_CHAR_LENGTH'
    assert Utils.SIZE.value == 41
    assert Utils.DB_NAME_ERROR.value == 'Invalid character'
    assert Utils.INVALID_CHAR_LENGTH.value == 'Incorrect number of characters'

def test_engine_attr():
    assert EngineAttr.TYPE_NAME.name == 'TYPE_NAME'
    assert EngineAttr.DB_NAME.name == 'DB_NAME'
    assert EngineAttr.ENGINE.name == 'ENGINE'
    assert EngineAttr.DOC.name == 'DOC'
    assert EngineAttr.VALUE_ERROR.name == 'VALUE_ERROR'
    assert EngineAttr.TYPE_NAME.value == 'EngineAttributes'
    assert EngineAttr.DB_NAME.value == 'db_name'
    assert EngineAttr.ENGINE.value == 'engine'
    assert EngineAttr.DOC.value == '''Defines a namedtuple for tuple returned by utils.setup_engine.
    Attributes:
        db_name (str): name of the database for this engine
        engine (Engine): the sqlalchemy engine object
    '''
    assert EngineAttr.VALUE_ERROR.value == 'No such engine found'


def test_meta_attr():
    assert MetaAttr.TYPE_NAME.name == 'TYPE_NAME'
    assert MetaAttr.DB_NAME.name == 'DB_NAME'
    assert MetaAttr.METADATA.name == 'METADATA'
    assert MetaAttr.DOC.name == 'DOC'
    assert MetaAttr.TYPE_NAME.value == 'MetaAttributes'
    assert MetaAttr.DB_NAME.value == 'db_name'
    assert MetaAttr.METADATA.value == 'metadata'
    assert MetaAttr.DOC.value == '''Defines a namedtuple for all metadata attributes of a LiteStash.
    Attributes:
        db_name (str): name of the database for this metadata
        metadata (Metadata): the sqlalchemy metadata object
    '''


def test_session_attr():
    assert SessionAttr.TYPE_NAME.name == 'TYPE_NAME'
    assert SessionAttr.DB_NAME.name == 'DB_NAME'
    assert SessionAttr.SESSION.name == 'SESSION'
    assert SessionAttr.VALUE_ERROR.name == 'VALUE_ERROR'
    assert SessionAttr.DOC.name == 'DOC'
    assert SessionAttr.TYPE_NAME.value == 'SessionAttributes'
    assert SessionAttr.DB_NAME.value == 'db_name'
    assert SessionAttr.SESSION.value == 'session'
    assert SessionAttr.VALUE_ERROR.value == 'Invalid database: no tables found'
    assert SessionAttr.DOC.value == '''Defines a namedtuple for all session attributes of a LiteStash.
    Attributes:
        db_name (str): name of the database for this session
        session (Session): the sqlalchemy session object
    '''

def test_engine_conf_attr():
    assert EngineConf.CACHE.name == 'CACHE'
    assert EngineConf.SQLITE.name == 'SQLITE'
    assert EngineConf.DIR_NAME.name == 'DIR_NAME'
    assert EngineConf.NAME_MIN_LENGTH.name == 'NAME_MIN_LENGTH'
    assert EngineConf.NAME_MAX_LENGTH.name == 'NAME_MAX_LENGTH'
    assert 'ECHO' in name_chk(EngineConf)
    assert 'FUTURE' in name_chk(EngineConf)
    assert 'NO_ECHO' in name_chk(EngineConf)
    assert 'NO_FUTURE' in name_chk(EngineConf)
    assert EngineConf.POOL_SIZE.name == 'POOL_SIZE'
    assert EngineConf.MAX_OVERFLOW.name == 'MAX_OVERFLOW'
    assert EngineConf.DB_NAME_SPACE.name == 'DB_NAME_SPACE'
    assert EngineConf.DB_NAME_ASCII.name == 'DB_NAME_ASCII'
    assert EngineConf.DB_NAME_LENGTH.name == 'DB_NAME_LENGTH'
    assert EngineConf.DIR_NOT_FOUND.name == 'DIR_NOT_FOUND'
    assert EngineConf.NO_DIR_ACCESS.name == 'NO_DIR_ACCESS'
    assert EngineConf.DIR_PATH_ERROR.name == 'DIR_PATH_ERROR'
    assert EngineConf.CACHE.value == ':memory:'
    assert EngineConf.SQLITE.value == 'sqlite:///'
    assert EngineConf.DIR_NAME.value == f'{Path.cwd()}/data'
    assert EngineConf.NAME_MIN_LENGTH.value == 3
    assert EngineConf.NAME_MAX_LENGTH.value == 128
    assert EngineConf.ECHO.value == True
    assert EngineConf.FUTURE.value == True
    assert EngineConf.NO_ECHO.value == False
    assert EngineConf.NO_FUTURE.value == False
    assert EngineConf.POOL_SIZE.value == 50
    assert EngineConf.MAX_OVERFLOW.value == 10
    assert EngineConf.DB_NAME_SPACE.value == 'No spaces permitted in database name'
    assert EngineConf.DB_NAME_ASCII.value == 'Database name permits only ASCII characters'
    assert EngineConf.DB_NAME_LENGTH.value == 'Invalid database name length provided'
    assert EngineConf.DIR_NOT_FOUND.value == 'No such file or directory'
    assert EngineConf.NO_DIR_ACCESS.value == 'Directory inaccessible'
    assert EngineConf.DIR_PATH_ERROR.value == 'Path Exception'


def test_engine_conf_methods():
    assert EngineConf.cache() == ':memory:'
    assert EngineConf.sqlite() == 'sqlite:///'
    assert EngineConf.dirname() == f'{Path.cwd()}/data'
    assert EngineConf.min_name_length() == 3
    assert EngineConf.max_name_length() == 128
    assert EngineConf.echo() == True
    assert EngineConf.future() == True
    assert EngineConf.no_echo() == False
    assert EngineConf.no_future() == False
    assert EngineConf.pool_size() == 50
    assert EngineConf.max_overflow() == 10
    assert EngineConf.db_name_space() == 'No spaces permitted in database name'
    assert EngineConf.db_name_ascii() == 'Database name permits only ASCII characters'
    assert EngineConf.db_name_length() == 'Invalid database name length provided'
    assert EngineConf.dir_not_found() == 'No such file or directory'
    assert EngineConf.no_dir_access() == 'Directory inaccessible'
    assert EngineConf.dir_path_error() == 'Path Exception'
