from manager import Manager
from db import Database
from worker import Worker, WorkerException
from instruction import Instruction


if __name__ == "__main__":
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
