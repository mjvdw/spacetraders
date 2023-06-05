import os
import requests
from dotenv import load_dotenv


class SpacetradersAPI(object):
    API_URL = "https://api.spacetraders.io/v2"
    ENV_API_TOKEN = "SPACETRADERS_API_TOKEN"

    def __init__(self, api_key: str = "") -> None:
        self.session = requests.session()

        load_dotenv()
        self.api_key = api_key
        self.callsign = os.getenv("CALLSIGN")
        self.email = os.getenv("EMAIL")

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
        # Happens weekly.
        if "error" in response.json():
            try:
                headers.pop("Authorization")
                register_response = self.session.request(
                    method="post",
                    url=f"{self.API_URL}/register",
                    headers=headers,
                    json={
                        "symbol": self.callsign,
                        "faction": "COSMIC",
                        "email": self.email,
                    },
                )
                token = register_response.json()
                print(register_response.json())
                os.environ[self.ENV_API_TOKEN] = token
            except Exception as error:
                print(
                    "Unable to register for an API token. Cannot send any other requests. Error: ",
                    error,
                )
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
