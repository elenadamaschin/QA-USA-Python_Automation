import data
import helpers  # Importing the helpers module


class TestUrbanRoutes:
    # Task 4: Setup class to check server status
    @classmethod
    def setup_class(cls):
        # Check if the Urban Routes server is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    # Task 3: Define test functions
    def test_set_route(self, self):
        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self, self):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self, self):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self, self):
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self, self):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self, self):
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    # Task 5: Preparing the ice cream order
    def test_order_2_ice_creams(self, self):
        """
        This test will prepare an order for 2 ice creams.
        We'll use a for loop to simulate the order process.
        """
        for i in range(2):  # Loop to simulate ordering two ice creams
            # Add in S8
            print(f"Adding ice cream #{i + 1} to the order")
            pass

    def test_car_search_model_appears(self, self):
        # Add in S8
        print("function created for car search model appears")
        pass

