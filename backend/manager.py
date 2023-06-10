from worker import Worker
from instruction import Instruction


class Manager(object):
    def __init__(self, db):
        self.db = db

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
    def next_instruction(self, i):
        self._next_instruction = i


class ManagerException(Exception):
    pass
