from spacetraders import SpaceTraders


class Worker(object):
    def __init__(self, instruction):
        self.instruction = instruction
        self.api = SpaceTraders()

    def go(self):
        print("Carrying out instruction")
        try:
            st_class = getattr(self.api, self.instruction.st_class)
            func = getattr(st_class, self.instruction.st_method)

            args = self.instruction.args

            inline_object = (
                {self.instruction.inline_object_name: self.instruction.payload}
                if self.instruction.has_payload
                else {}
            )

            res = func(**args, **inline_object) if args else func(**inline_object)
            return res
        except Exception as e:
            print("Error: ", e)


class WorkerException(Exception):
    pass
