import os
import sqlite3
from instruction import Instruction


class Database(object):
    DB_NAME = "state.db"

    def __init__(self):
        pass

    def _connect(self):
        parent_dir = os.path.abspath(os.path.dirname(__file__))
        conn = sqlite3.connect(f"{parent_dir}/{self.DB_NAME}")
        c = conn.cursor()
        return c

    def _create_table(self, table_name: str, base_object: object) -> None:
        pass

    def add_record_to_table(self, table: str, record: Instruction | object) -> None:
        self._create_table("test", Instruction)
        c = self._connect()
        pass
