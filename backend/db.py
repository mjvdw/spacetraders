import os
import sqlite3


class Database(object):
    def __init__(self):
        parent_dir = os.path.abspath(os.path.dirname(__file__))
        self.conn = sqlite3.connect(f"{parent_dir}/state.db")
