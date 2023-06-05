from utils import pprint
from spacetraders import SpacetradersAPI

if __name__ == "__main__":
    st = SpacetradersAPI()

    # List current contracts.
    contracts = st.list_contracts()

    # Accept the first contract in the list.
    contract_id = contracts["data"][0]["id"]
    response = st.accept_contract(contract_id=contract_id)
    pprint(response)
