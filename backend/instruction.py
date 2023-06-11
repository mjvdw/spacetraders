import openapi_client


class Instruction(object):
    def __init__(self, instruction_parameters):
        self.params = instruction_parameters

    @property
    def payload(self):
        return openapi_client.InlineObject2(**self.params["payload"])

    @property
    def inline_object_name(self):
        return "inline_object2"
