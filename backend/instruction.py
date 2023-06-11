import openapi_client
from typing import Dict


class Instruction(object):
    def __init__(
        self,
        name: str,
        st_class: str,
        st_method: str,
        args: dict = {},
        payload: Dict[str, dict] = {"object_type": "", "body": {}},
    ):
        self.name = name
        self.st_class = st_class
        self.st_method = st_method
        self.args = args
        self._payload = payload

    @property
    def payload(self):
        if self._payload["body"]:
            func = getattr(openapi_client, self._payload["object_type"])
            return func(**self._payload["body"])
        else:
            return self._payload

    @property
    def inline_object_name(self):
        base = "inline_object"
        suffix = self._payload["object_type"][len("InlineObject") :]
        return base + suffix

    @property
    def has_payload(self):
        return self._payload["body"] != {}
