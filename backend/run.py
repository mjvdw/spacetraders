from db import Database
from manager import Manager
from worker import Worker, WorkerException
from instruction import Instruction
from utils import SpaceTraderClass

# Enter a context with an instance of the API client
db = Database()
manager = Manager(db=db)

TEST = {
    "http_request": "POST",
    "name": "My agent details",
    "class": SpaceTraderClass.FLEET.value,
    "method": "purchase_ship",
    "args": None,
    "payload": {"ship_type": "SHIP_MINING_DRONE", "waypoint_symbol": "X1-KS52-23717D"},
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
