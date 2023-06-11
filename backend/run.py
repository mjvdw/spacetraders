from spacetraders import SpaceTraders, SpaceTradersException
from pprint import pprint


# Enter a context with an instance of the API client
st = SpaceTraders()
try:
    api_response = st.default.get_status()
    pprint(api_response)
except SpaceTradersException as error:
    print(error)
