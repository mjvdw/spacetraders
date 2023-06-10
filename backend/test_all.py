from manager import Manager
from worker import Worker, WorkerException
from db import Database
from instruction import Instruction


def test_run():
    db = Database()
    manager = Manager(db=db)

    TEST = {
        "name": "My agent details",
        "api_command": "get_my_agent_details",
        "params": None,
    }

    manager.next_instruction = Instruction(TEST)

    if manager.has_instruction:
        worker = Worker(manager.next_instruction)
        try:
            worker.go()
        except WorkerException as e:
            print(e)
