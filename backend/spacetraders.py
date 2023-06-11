from __future__ import print_function
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv


class SpaceTraders(object):
    # Static variables
    API_URL = "https://api.spacetraders.io/v2"
    ENV_API_TOKEN = "SPACETRADERS_API_TOKEN"

    def __init__(self):
        # Set up openapi configuration.
        load_dotenv()
        api_key = os.getenv(self.ENV_API_TOKEN)
        self.configuration = openapi_client.Configuration(
            host="https://api.spacetraders.io/v2"
        )
        self.configuration.access_token = api_key
        self.api_client = openapi_client.ApiClient(self.configuration)

    @property
    def default(self):
        return openapi_client.DefaultApi(self.api_client)

    @property
    def agents(self):
        return openapi_client.AgentsApi(self.api_client)

    @property
    def contracts(self):
        return openapi_client.ContractsApi(self.api_client)

    @property
    def factions(self):
        return openapi_client.FactionsApi(self.api_client)

    @property
    def fleet(self):
        return openapi_client.FleetApi(self.api_client)

    @property
    def systems(self):
        return openapi_client.SystemsApi(self.api_client)


class SpaceTradersException(ApiException):
    pass
