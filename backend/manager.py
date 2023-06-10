from worker import Worker
from instruction import Instruction


class Manager(object):
    def __init__(self, api, db):
        self.api = api
        self.db = db

    def give_instruction(self, worker: Worker, instruction: Instruction) -> bool:
        return True

    def create_instruction(self):
        return True

    @property
    def has_instruction(self) -> bool:
        return True

    @property
    def next_instruction(self) -> Instruction:
        i = Instruction("Test instruction")
        return i


class ManagerException(Exception):
    pass
