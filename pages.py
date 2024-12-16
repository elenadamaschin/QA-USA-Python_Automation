from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class UrbanRoutesPage:
    """
    Page Object Model for Urban Routes application.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    START_ADDRESS = (By.CSS_SELECTOR, "#from")
    END_ADDRESS = (By.CSS_SELECTOR, "#to")
    TAXI_MODE_SUPPORTIVE = (By.CSS_SELECTOR, "#supportive")
    PHONE_INPUT = (By.CSS_SELECTOR, "#phone")
    CARD_INPUT = (By.CSS_SELECTOR, "#number")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "#comment")
    BLANKET_CHECKBOX = (By.CSS_SELECTOR, ".switch.blanket-checkbox")
    HANDKERCHIEF_CHECKBOX = (By.CSS_SELECTOR, ".switch-input.handkerchief-checkbox")
    ICE_CREAM_PLUS = (By.CSS_SELECTOR, "button.ice-cream-plus")  # Updated for button specificity
    ICE_CREAM_COUNTER = (By.CSS_SELECTOR, ".counter-value")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@id='place-order']")

    # Methods
    def set_route(self, start_address: str, end_address: str):
        """
        Set the start and end addresses for the route.
        """
        start_input = self.driver.find_element(*self.START_ADDRESS)
        start_input.clear()
        start_input.send_keys(start_address)

        end_input = self.driver.find_element(*self.END_ADDRESS)
        end_input.clear()
        end_input.send_keys(end_address)

    def get_from(self) -> str:
        """
        Get the current value of the 'start address' field.
        """
        return self.driver.find_element(*self.START_ADDRESS).get_attribute("value")

    def get_to(self) -> str:
        """
        Get the current value of the 'end address' field.
        """
        return self.driver.find_element(*self.END_ADDRESS).get_attribute("value")

    def select_supportive_mode(self):
        """
        Select the supportive taxi mode.
        """
        self.driver.find_element(*self.TAXI_MODE_SUPPORTIVE).click()

    def is_supportive_mode_selected(self) -> bool:
        """
        Check if supportive taxi mode is selected.
        """
        return self.driver.find_element(*self.TAXI_MODE_SUPPORTIVE).is_selected()

    def fill_phone_number(self, phone: str):
        """
        Enter the phone number for the order.
        """
        phone_input = self.driver.find_element(*self.PHONE_INPUT)
        phone_input.clear()
        phone_input.send_keys(phone)

    def get_phone_number(self) -> str:
        """
        Get the current value of the phone number field.
        """
        return self.driver.find_element(*self.PHONE_INPUT).get_attribute("value")

    def fill_card_details(self, card: str):
        """
        Enter the card details for payment.
        """
        card_input = self.driver.find_element(*self.CARD_INPUT)
        card_input.clear()
        card_input.send_keys(card)

    def get_card_number(self) -> str:
        """
        Get the current value of the card number field.
        """
        return self.driver.find_element(*self.CARD_INPUT).get_attribute("value")

    def add_message_to_driver(self, message: str):
        """
        Add a message for the driver.
        """
        message_input = self.driver.find_element(*self.MESSAGE_INPUT)
        message_input.clear()
        message_input.send_keys(message)

    def get_driver_message(self) -> str:
        """
        Get the current value of the driver message field.
        """
        return self.driver.find_element(*self.MESSAGE_INPUT).get_attribute("value")

    def select_extras(self):
        """
        Select extras (blanket and handkerchief).
        """
        self.driver.find_element(*self.BLANKET_CHECKBOX).click()
        self.driver.find_element(*self.HANDKERCHIEF_CHECKBOX).click()

    def is_blanket_selected(self) -> bool:
        """
        Check if the blanket checkbox is selected.
        """
        return self.driver.find_element(*self.BLANKET_CHECKBOX).is_selected()

    def is_handkerchief_selected(self) -> bool:
        """
        Check if the handkerchief checkbox is selected.
        """
        return self.driver.find_element(*self.HANDKERCHIEF_CHECKBOX).is_selected()

    def add_ice_cream(self, count: int):
        """
        Add ice creams to the order.
        """
        ice_cream_plus = self.driver.find_element(*self.ICE_CREAM_PLUS)
        for _ in range(count):
            ice_cream_plus.click()

    def get_ice_cream_count(self) -> int:
        """
        Get the current count of ice creams added to the order.
        """
        return int(self.driver.find_element(*self.ICE_CREAM_COUNTER).text)

    def place_order(self):
        """
        Place the order.
        """
        self.driver.find_element(*self.PLACE_ORDER_BUTTON).click()

    def is_car_search_model_visible(self) -> bool:
        """
        Check if the car search model is visible after placing the order.
        """
        return self.driver.find_element(By.ID, "car-search-model").is_display
