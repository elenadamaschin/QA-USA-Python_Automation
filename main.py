import helpers
import data
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """
        Setup method to initialize WebDriver and verify the server status.
        """
        # Check if the Urban Routes server is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

        # Set up WebDriver with logging capabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    @classmethod
    def teardown_class(cls):
        """
        Teardown method to close the WebDriver.
        """
        cls.driver.quit()
