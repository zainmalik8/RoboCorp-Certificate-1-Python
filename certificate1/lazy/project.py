"""
RPA is framework of automation which has different library like Selenium, Desktop and
many more

"""

from RPA.Browser.Selenium import Selenium
import time


class CertificateOne:

    def __init__(self, username, password):
        """
        Initiating some Variables that will help soon
        """
        self.browser = Selenium()

        self.username = username
        self.password = password

    def open_browser(self):
        """
        open browser with specific Uniform Resource Locator (URL)
        """
        self.browser.open_available_browser(url="https://robotsparebinindustries.com/")

    def login(self):
        """
        To enter text in Input fields you have to interact with X-paths,
        So read it's documentation or watch Tutorials(IF YOU ARE DUMB LIKE ME)
        """

        """
        And I swear input_text_when_element_is_visible is more Efficient than just input_text,
        For more Information..Go TO Sweet Davis's Hell
        """

        """
        # self.browser.input_password(locator="//input[contains(@id, 'pass')]", password='thoushallnotpass', clear=True)
        I tried it also try to debug it .. But You know my debugging skill.

        """

        """
        You can also use these for click
        `self.browser.find_element(locator="//button[contains(@class, 'btn-primary')]").click()
        self.browser.click_element_when_visible(locator="//button[contains(@class, 'btn-primary')]")
        """
        while True:
            try:
                self.browser.input_text_when_element_is_visible(locator="//input[contains(@id, 'name')]",
                                                                text=self.username)
                time.sleep(1)
                self.browser.input_text_when_element_is_visible(locator="//input[contains(@id, 'pass')]",
                                                                text=self.password)
                self.browser.click_button_when_visible(locator="//button[contains(@class, 'btn-primary')]")
                self.browser.wait_until_page_contains_element(locator="//input[contains(@name, 'first')]")
                time.sleep(1)
            except Exception:
                pass
            else:
                break
            finally:
                print("DON't worry")
