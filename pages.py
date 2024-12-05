from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class UrbanRoutesPage:
    """
    Page Object Model for Urban Routes application.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    START_ADDRESS = (By.ID, "start-address")
    END_ADDRESS = (By.ID, "end-address")
    TAXI_MODE_SUPPORTIVE = (By.CLASS_NAME, "taxi-mode-supportive")
    PHONE_INPUT = (By.ID, "phone-number")
    CARD_INPUT = (By.ID, "card-details")
    MESSAGE_INPUT = (By.ID, "driver-message")
    BLANKET_CHECKBOX = (By.ID, "blanket")
    HANDKERCHIEF_CHECKBOX = (By.ID, "handkerchiefs")
    ICE_CREAM_DROPDOWN = (By.ID, "ice-cream-options")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@id='place-order']")

    # Methods
    def set_route(self, start_address: str, end_address: str):
        self.driver.find_element(*self.START_ADDRESS).send_keys(start_address)
        self.driver.find_element(*self.END_ADDRESS).send_keys(end_address)

    def select_supportive_mode(self):
        self.driver.find_element(*self.TAXI_MODE_SUPPORTIVE).click()

    def fill_phone_number(self, phone: str):
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def fill_card_details(self, card: str):
        self.driver.find_element(*self.CARD_INPUT).send_keys(card)

    def add_message_to_driver(self, message: str):
        self.driver.find_element(*self.MESSAGE_INPUT).send_keys(message)

    def select_extras(self):
        self.driver.find_element(*self.BLANKET_CHECKBOX).click()
        self.driver.find_element(*self.HANDKERCHIEF_CHECKBOX).click()

    def add_ice_cream(self, count: int):
        dropdown = self.driver.find_element(*self.ICE_CREAM_DROPDOWN)
        for _ in range(count):
            dropdown.click()

    def place_order(self):
        self.driver.find_element(*self.PLACE_ORDER_BUTTON).click()