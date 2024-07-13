"""The Storage module

Define the LiteStash key-value database object.
LiteStash is a text key with JSON value key value store.
"""
from litestash.core.config.litestash_conf import StashSlots
from litestash.core.engine import Engine
from litestash.core.schema import Metadata
from litestash.core.session import Session
from litestash.models import LiteStashData
from litestash.core.util.litestash_util import hash_key
from litestash.core.util.litestash_util import check_key
from litestash.core.util.schema_util import get_db_name
from litestash.core.util.schema_util import get_table_name
from sqlalchemy import select
from pydantic import ValidationError

class LiteStash:
    """The LiteStash

    TODO
    """
    __slots__ = (StashSlots.ENGINE.value,
                 StashSlots.METADATA.value,
                 StashSlots.DB_SESSION.value
    )

    def __init__(self):
        """Initiate a new LiteStash

        Creates a new empty cache by default.
        """
        self.engine = Engine()
        self.metadata = Metadata(self.engine)
        self.db_session = Session(self.engine)


    def set(self, key: str, value: str) -> None:
        """LiteStash Key Setter

        Add a new key to the database.
        If key already exists update the value.
        """
        pass

    def get(self, key: str) -> LiteStashData | None:
        """LiteStash Get a value.

        Given a key return the value stored.
        Returns the key,value as LiteStashData.
        Args:
            key (str): The key for the json data
        """
        # update with logger and review validation
        try:
            # create the LSD DTO with given str
            dto = LiteStashData(key=check_key(key))
        except ValidationError as e:
            print(f'Invalid key: {e}')
        # return hash byte with utils.hash_key function
        hashed_key = hash_key(dto.key)
        # utils find db name for the given key hash (strip .db off)
        db_name = get_db_name(hashed_key[0])[:3].decode()
        # utils get the table name
        table_name = get_table_name(hashed_key)
        # extract metadata for db_name
        metadata = getattr(self.metadata, db_name).metadata
        # the table for the select
        table = metadata.tables[table_name]
        # assemble the sql
        sql_statement = select(table).where(table.c.key_hash == hashed_key)
        # extract session for db_name
        session = getattr(self.db_session, db_name).session
        # get the data
        data = session.execute(sql_statement)
        if data:
            return LiteStashData(
                key=data.key,
                value=data.value
            )
        else:
            return None



    def delete(self):
        """LiteStash Delete

        Remove a give key and its value from the database.
        """
        pass

    def keys(self):
        """ListStash Keys"""
        pass

    def values(self):
        """Return all values from database in a dictionary."""
        pass

    def exists(self, key: str) -> bool:
        """Check if key exists and return true if it does."""


    def clear(self) -> None:
        """Clear all entries from the database."""
        pass

    def __repr__(self) -> str:
        """Detailed string representation"""
        pass

    def __str__(self) -> str:
        """Quick and minimal string"""
        pass
#@event.listens_for(Engine, 'connect')
#def pragma_setup(db_connection, connection):
#    """Pragma setup
#    Turn on WAL mode, normal sync, and foreign_keys.
#    Leave the rest to sqlite defaults.
#    """
#    cursor = db_connection.cursor()
#    cursor.execute(Pragma.journal_mode())
#    cursor.execute(Pragma.synchronous())
#    cursor.execute(Pragma.foreign_keys())
#    cursor.close()
