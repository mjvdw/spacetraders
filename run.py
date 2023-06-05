from spacetraders import SpacetradersAPI

if __name__ == "__main__":
    st = SpacetradersAPI()
    print(st.get_status())
