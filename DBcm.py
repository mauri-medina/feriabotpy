import mysql.connector
from config import DB_CONFIG


class UseDataBase:
    """ContextManager for mysql operations"""

    def __init__(self) -> None:
        self.configuration = DB_CONFIG

    def __enter__(self) -> 'cursor':
        self.connection = mysql.connector.connect(**self.configuration)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
