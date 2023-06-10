import spacetraders


class Worker(object):
    def __init__(self, instruction):
        self.instruction = instruction
        self.api = spacetraders.SpacetradersAPI()

    def go(self) -> bool:
        print("Carrying out instruction")
        try:
            func = getattr(self.api, self.instruction.params["api_command"])
            res = func()
            print(res)
        except Exception as e:
            print(e)
            return False
        else:
            return True


class WorkerException(Exception):
    pass
