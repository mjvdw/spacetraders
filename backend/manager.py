from db import Database
from instruction import Instruction

from pprint import pprint


class Manager(object):
    def __init__(self, db: Database = Database()):
        self.db = db

    def supervise(self, worker_response):
        pprint(worker_response)

    def _write_instruction(self) -> bool:
        return True

    def _read_instruction(self) -> bool:
        return True

    @property
    def has_instruction(self) -> bool:
        return True

    @property
    def next_instruction(self) -> Instruction:
        return self._next_instruction

    @next_instruction.setter
    def next_instruction(self, instruction):
        self._next_instruction = instruction

    def add_instruction(self, instruction: Instruction) -> None:
        self.db.add_record_to_table("instructions", instruction)


class ManagerException(Exception):
    pass
