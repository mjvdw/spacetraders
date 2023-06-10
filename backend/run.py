from manager import Manager
from db import Database
from worker import Worker, WorkerException
from spacetraders import SpacetradersAPI


if __name__ == "__main__":
    st = SpacetradersAPI()
    db = Database()
    manager = Manager(api=st, db=db)

    if manager.has_instruction:
        worker = Worker(manager.next_instruction)
        try:
            worker.go()
        except WorkerException as e:
            print(e)

    # If there are instructions pending:
    #   Take first instruction off the top of the list.
    #   Start up worker to complete first instruction.
    # Else, if there are no instructions:
    #   Get open contracts and select one to kick of the
    #   cycle again.

    # While true loop here?
    # Or somehow start some service if that's no sustainable.
