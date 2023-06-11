from db import Database
from manager import Manager
from worker import Worker, WorkerException
from instruction import Instruction
from utils import SpaceTraderClass

# Enter a context with an instance of the API client
db = Database()
manager = Manager(db=db)

TEST = {
    "name": "My agent details",
    "class": SpaceTraderClass.DEFAULT.value,
    "method": "get_status",
    "params": None,
}

manager.next_instruction = Instruction(TEST)

if manager.has_instruction:
    worker = Worker(manager.next_instruction)
    try:
        worker.go()
    except WorkerException as e:
        print(e)
