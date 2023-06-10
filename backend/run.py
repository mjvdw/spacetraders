from utils.general import pprint
from utils.spacetraders import SpacetradersAPI

if __name__ == "__main__":
    st = SpacetradersAPI()

    info = st.get_my_agent_details()
    print(info)

    # List current contracts.
    # contracts = st.list_contracts()

    # Accept the first contract in the list.
    # contract_id = contracts["data"][0]["id"]
    # response = st.accept_contract(contract_id=contract_id)
    # pprint(response)
