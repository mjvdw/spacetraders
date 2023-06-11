from spacetraders import SpaceTraders


class Worker(object):
    def __init__(self, instruction):
        self.instruction = instruction
        self.api = SpaceTraders()

    def go(self):
        print("Carrying out instruction")
        try:
            st_class = getattr(self.api, self.instruction.params["class"])
            func = getattr(st_class, self.instruction.params["method"])

            args = self.instruction.params["args"]

            inline_object = {
                self.instruction.inline_object_name: self.instruction.payload
            }

            res = func(**args, **inline_object) if args else func(**inline_object)
            return res
        except Exception as e:
            print(e)


class WorkerException(Exception):
    pass
