from db import Database
from manager import Manager
from worker import Worker, WorkerException
from instruction import Instruction
from utils import SpaceTraderClass
import openapi_client

# Enter a context with an instance of the API client
db = Database()
manager = Manager(db=db)

manager.next_instruction = Instruction(
    name="My agent details",
    st_class=SpaceTraderClass.DEFAULT.value,
    st_method="register",
    args=None,
    payload={
        "object_type": "InlineObject",
        "body": {"faction": "COSMIC", "symbol": "BORING_TEST"},
    },
)


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
