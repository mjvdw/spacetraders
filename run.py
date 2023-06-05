from spacetraders import SpacetradersAPI

if __name__ == "__main__":
    st = SpacetradersAPI()

    # List current contracts.

    contracts = st.list_contracts()
