# from manager import Manager
# from db import Database
# from worker import Worker, WorkerException
# from instruction import Instruction


# if __name__ == "__main__":
#     # db = Database()
#     # manager = Manager(db=db)

#     # TEST = {
#     #     "name": "My agent details",
#     #     "api_command": "get_my_agent_details",
#     #     "params": None,
#     # }

#     # manager.next_instruction = Instruction(TEST)

#     # if manager.has_instruction:
#     #     worker = Worker(manager.next_instruction)
#     #     try:
#     #         worker.go()
#     #     except WorkerException as e:
#     #         print(e)

#     pass

from __future__ import print_function

import time
import openapi_client

from openapi_client.rest import ApiException
from pprint import pprint
import os
from dotenv import load_dotenv


API_URL = "https://api.spacetraders.io/v2"
ENV_API_TOKEN = "SPACETRADERS_API_TOKEN"
ENV_CALLSIGN = "CALLSIGN"
ENV_EMAIL = "EMAIL"

load_dotenv()
api_key = os.getenv(ENV_API_TOKEN)
callsign = os.getenv(ENV_CALLSIGN)
email = os.getenv(ENV_EMAIL)

configuration = openapi_client.Configuration(host="https://api.spacetraders.io/v2")
configuration.access_token = api_key


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AgentsApi(api_client)
    try:
        # Get Agent
        api_response = api_instance.get_my_agent()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentsApi->get_my_agent: %s\n" % e)
