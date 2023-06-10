class Worker(object):
    def __init__(self, instruction):
        self.instruction = instruction

    def go(self) -> bool:
        print("Carrying out instruction")
        return True


class WorkerException(Exception):
    pass
