from spacetraders import SpaceTraders
from pprint import pprint


class Worker(object):
    def __init__(self, instruction):
        self.instruction = instruction
        self.api = SpaceTraders()

    def go(self) -> bool:
        print("Carrying out instruction")
        try:
            st_class = getattr(self.api, self.instruction.params["class"])
            func = getattr(st_class, self.instruction.params["method"])
            res = func()
            print(res)
        except Exception as e:
            print(e)
            return False
        else:
            return True


class WorkerException(Exception):
    pass
