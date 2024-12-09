import data
import helpers  # Correctly import helpers for server reachability check
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage  # Import the page object class


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Enable logging for performance monitoring
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)
        
        # Check if the server is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):  # Correctly call the method from helpers
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")
        
        # Initialize the page object
        cls.page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
        """
        Test setting the route with given 'from' and 'to' addresses.
        Verifies that the input fields are correctly populated.
        """
        self.driver.get(data.URBAN_ROUTES_URL)  # Navigate to the Urban Routes app
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        """
        Test selecting the supportive mode taxi plan.
        Verifies that the selection is successful.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_taxi_mode()
        assert routes_page.is_supportive_mode_selected()

    def test_fill_phone_number(self):
        """
        Test adding the phone number to the order.
        Verifies the phone number input field is populated.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_phone_number(data.PHONE_NUMBER)
        assert routes_page.get_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        """
        Test adding card details for payment.
        Verifies the card number and code input fields are populated.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_card_details(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.get_card_number() == data.CARD_NUMBER
        assert routes_page.get_card_code() == data.CARD_CODE

    def test_comment_for_driver(self):
        """
        Test adding a comment for the driver.
        Verifies the comment input field is populated.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_driver_message() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        """
        Test adding extras (blanket and handkerchiefs) to the order.
        Verifies the selections are made.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_extras()
        assert routes_page.is_blanket_selected()
        assert routes_page.is_handkerchief_selected()

    def test_order_2_ice_creams(self):
        """
        Test adding two ice creams to the order.
        Verifies the ice cream count.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_ice_creams(count=2)
        assert routes_page.get_ice_cream_count() == 2

    def test_car_search_model_appears(self):
        """
        Test placing the order.
        Verifies that the car search model appears after placing the order.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.place_order()
        assert routes_page.is_car_search_model_visible()
