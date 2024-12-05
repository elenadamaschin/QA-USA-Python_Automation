import data
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Enable logging for performance monitoring
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

        # Check if the server is reachable
        if is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server.")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running.")

        cls.page = UrbanRoutesPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_set_route(self):
        self.page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

    def test_select_plan(self):
        self.page.select_supportive_mode()

    def test_fill_phone_number(self):
        self.page.add_phone_number(data.PHONE_NUMBER)

    def test_fill_card(self):
        self.page.add_card(data.CARD_NUMBER)

    def test_comment_for_driver(self):
        self.page.add_message_for_driver(data.MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        self.page.add_blanket_and_handkerchiefs()

    def test_order_2_ice_creams(self):
        self.page.add_ice_cream(quantity=2)

    def test_car_search_model_appears(self):
        self.page.place_order()
