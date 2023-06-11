from __future__ import print_function
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
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
