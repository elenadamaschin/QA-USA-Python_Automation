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
    def test_set_route(self):
        """
        Test setting a route using Urban Routes.
        """
        print("Function created for set route")

    def test_select_plan(self):
        """
        Test selecting a supportive taxi mode.
        """
        print("Function created for select plan")

    def test_fill_phone_number(self):
        """
        Test filling in a phone number.
        """
        print("Function created for fill phone number")

    def test_fill_card(self):
        """
        Test adding a card payment method.
        """
        print("Function created for fill card")

    def test_comment_for_driver(self):
        """
        Test adding a message to the driver.
        """
        print("Function created for comment for driver")

    def test_order_blanket_and_handkerchiefs(self):
        """
        Test adding a blanket and handkerchiefs to the order.
        """
        print("Function created for order blanket and handkerchiefs")

    # Task 5: Preparing the ice cream order
    def test_order_2_ice_creams(self):
        """
        Test ordering two ice creams.
        """
        ice_cream_count = 2  # Declare a variable for the number of ice creams
        for i in range(ice_cream_count):  # Use the variable in the range
            print(f"Adding ice cream #{i + 1} to the order")  # Simulate the ordering process

    def test_car_search_model_appears(self):
        """
        Test that searching for a car model displays results.
        """
        print("Function created for car search model appears")
