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
    "class": SpaceTraderClass.FLEET.value,
    "method": "get_my_ships",
    "params": None,
}

manager.next_instruction = Instruction(TEST)

if manager.has_instruction:
    worker = Worker(manager.next_instruction)
    try:
        manager.supervise(worker.go())
    except WorkerException as e:
        print(e)
else:
    # Figure out what the next action should be based on the current state.
    # Most likely just see what contracts are available and go for one of them.
    pass
