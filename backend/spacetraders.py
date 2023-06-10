import os
import requests
from dotenv import load_dotenv


class SpacetradersAPI(object):
    API_URL = "https://api.spacetraders.io/v2"
    ENV_API_TOKEN = "SPACETRADERS_API_TOKEN"
    ENV_CALLSIGN = "CALLSIGN"
    ENV_EMAIL = "EMAIL"

    def __init__(self) -> None:
        self.session = requests.session()

        load_dotenv()
        self.api_key = os.getenv(self.ENV_API_TOKEN)
        self.callsign = os.getenv(self.ENV_CALLSIGN)
        self.email = os.getenv(self.ENV_EMAIL)

    def _send_request(self, method: str, endpoint: str = "", body: dict = {}) -> dict:
        """Send a request to the Spacetraders.io API.

        Args:
            method (str): "GET", "POST", etc
            endpoint (str, optional): The API endpoint after the base URL. Defaults to "".
            body (dict, optional): Any body parameters that are part of the request. Defaults to {}.

        Returns:
            dict: The relevant object returned by the API.
        """

        url = self.API_URL + endpoint
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv(self.ENV_API_TOKEN)}",
        }
        response = self.session.request(
            method=method, url=url, headers=headers, params=body
        )

        # Handle error after server reset where token has been revoked.
        # Server reset happens weekly.
        if not str(response.status_code).startswith("2"):
            raise SpacetradersAPIException(response)
        else:
            return response.json()

    ###################
    # BASIC FUNCTIONS #
    ###################

    def get_my_agent_details(self) -> dict:
        """Get your agent's details.
        See: https://spacetraders.stoplight.io/docs/spacetraders/eb030b06e0192-my-agent-details

        Returns:
            dict: Agents details.
        """
        return self._send_request(method="get", endpoint="/my/agent")

    def get_status(self) -> dict:
        """Return the status of the game server.

        Returns:
            dict: The status of the game server.
        """
        return self._send_request(method="get")

    ######################
    # CONTRACT FUNCTIONS #
    ######################

    def list_contracts(self) -> dict:
        return self._send_request(method="get", endpoint="/my/contracts")

    def accept_contract(self, contract_id: str) -> dict:
        return self._send_request(
            method="POST", endpoint=f"/my/contracts/{contract_id}/accept"
        )


class SpacetradersAPIException(Exception):
    """Display and handle spacetraders API specific errors."""

    def __init__(self, response):
        self.code = 0
        try:
            json_res = response.json()
        except ValueError:
            self.message = f"Invalid error message: {response.text}"
        else:
            self.code = json_res["error"]["code"]
            self.message = json_res["error"]["message"]

        self.status_code = response.status_code
        self.response = response
        self.request = getattr(response, "request", None)

    def __str__(self):
        return (
            f"HTTP(code={self.status_code}), API(errorcode={self.code}): {self.message}"
        )
