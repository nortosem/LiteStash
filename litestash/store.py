"""

TODO:
Optimized for Strings: Since all keys are strings, this approach is tailored specifically to that data type.
Consistent Hashing: You can still benefit from hashing all keys to ensure a more even distribution across tables, even if the first character distribution in your keys is not uniform.
Hash Collision Handling: Even with a good hash function, collisions are possible. You might want to consider a collision resolution strategy (e.g., chaining) within each table.
"""
from os import getcwd
from litestash.model import
from litestash.utils import
from litestash.config import Pragma
from litestash.config import SetupDB
from sqlalchemy import event
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


@event.listens_for(Engine, "connect")
def pragma_setup(db_connection, connection):
    """Pragma setup

    Turn on WAL mode, normal sync, and foreign_keys.
    Leave the reat to sqlite defaults.
    """
    cursor = db_connection.cursor()
    cursor.execute(Pragma.journal_mode())
    cursor.execute(Pragma.synchronous())
    cursor.execute(Pragma.foreign_keys())
    cursor.close()















engine = create_engine(
    f'{SetupDB.sqlite()}{getcwd()}{SetupDB.filename()}',
    echo=SetupDB.echo.value
)


