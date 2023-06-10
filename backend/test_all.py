from manager import Manager
from db import Database
from spacetraders import SpacetradersAPI


def test_manager():
    st = SpacetradersAPI()
    db = Database()
    manager = Manager(st, db)
    manager = Manager(api=st, db=db)

    assert manager.has_instruction == True
