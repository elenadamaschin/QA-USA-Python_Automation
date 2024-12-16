import data
import helpers  # Correctly import helpers for server reachability check
from pages import UrbanRoutesPage  # Import the page object class
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """
        Setup class for initializing the WebDriver and page object.
        Enables logging for performance monitoring.
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.add_experimental_option("goog:loggingPrefs", {'performance': 'ALL'})
        
        cls.driver = webdriver.Chrome(options=chrome_options)

        # Check if the server is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

        # Initialize the page object
        cls.page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        """
        Quit the WebDriver after all tests.
        """
        cls.driver.quit()

    def test_set_route(self):
        """
        Test setting the route with given 'from' and 'to' addresses.
        Verifies that the input fields are correctly populated.
        """
        self.driver.get(data.URBAN_ROUTES_URL)  # Navigate to the Urban Routes app
        self.page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from() == data.ADDRESS_FROM, "Start address did not match."
        assert self.page.get_to() == data.ADDRESS_TO, "End address did not match."

    def test_select_plan(self):
        """
        Test selecting the supportive mode taxi plan.
        Verifies that the selection is successful.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.select_supportive_mode()
        assert self.page.is_supportive_mode_selected(), "Supportive mode not selected."

    def test_fill_phone_number(self):
        """
        Test adding the phone number to the order.
        Verifies the phone number input field is populated.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.fill_phone_number(data.PHONE_NUMBER)
        assert self.page.get_phone_number() == data.PHONE_NUMBER, "Phone number did not match."

    def test_fill_card(self):
        """
        Test adding card details for payment.
        Verifies the card number input field is populated.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.fill_card_details(data.CARD_NUMBER)
        assert self.page.get_card_number() == data.CARD_NUMBER, "Card number did not match."

    def test_comment_for_driver(self):
        """
        Test adding a comment for the driver.
        Verifies the comment input field is populated.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.add_message_to_driver(data.MESSAGE_FOR_DRIVER)
        assert self.page.get_driver_message() == data.MESSAGE_FOR_DRIVER, "Driver message did not match."

    def test_order_blanket_and_handkerchiefs(self):
        """
        Test adding extras (blanket and handkerchiefs) to the order.
        Verifies the selections are made.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.select_extras()
        assert self.page.is_blanket_selected(), "Blanket checkbox not selected."
        assert self.page.is_handkerchief_selected(), "Handkerchief checkbox not selected."

    def test_order_2_ice_creams(self):
        """
        Test adding two ice creams to the order.
        Verifies the ice cream count.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.add_ice_cream(count=2)
        assert self.page.get_ice_cream_count() == 2, "Ice cream count did not match."

    def test_car_search_model_appears(self):
        """
        Test placing the order.
        Verifies that the car search model appears after placing the order.
        """
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page.place_order()
        assert self.page.is_car_search_model_visible(), "Car search model did not appear."
