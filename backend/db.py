import os
import sqlite3

parent_dir = os.path.abspath(os.path.dirname(__file__))
conn = sqlite3.connect(f"{parent_dir}/state.db")

print("Successfully opened database!")
