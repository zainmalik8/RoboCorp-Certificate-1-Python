"""
RPA is framework of automation which has different library like Selenium, Desktop and
many more

"""

from datetime import timedelta

from RPA.Browser.Selenium import Selenium
from RPA.Excel.Files import Files
from RPA.HTTP import HTTP
from RPA.PDF import PDF
from RPA.Tables import Table

from logger import logger
from .mappers import XpathMapper


class Process(XpathMapper):

    def __init__(self, username: str, password: str, output_path: str, sales_file_url: str):
        """
        Initiating certificate
        """
        self.browser = Selenium(auto_close=False)
        self.http, self.file, self.pdf = HTTP(), Files(), PDF()
        self.sheet_data: Table = Table()

        self.username, self.password = username, password
        self.downloading_path, self.sales_file_url = output_path, sales_file_url
        self.sales_entries: int = 0

    def open_browser(self):
        """
        open browser with specific Uniform Resource Locator (URL)
        """
        self.browser.open_available_browser(url="https://robotsparebinindustries.com/", maximized=True)

    def login(self):
        logger.info("Loging in....")

        self.browser.wait_until_page_contains_element(self.username_field,
                                                      timeout=timedelta(seconds=20))
        self.browser.input_text_when_element_is_visible(locator=self.username_field,
                                                        text=self.username)
        self.browser.input_text_when_element_is_visible(locator=self.password_field,
                                                        text=self.password)
        self.browser.click_button_when_visible(locator=self.generic_button)

        self.browser.wait_until_page_contains_element(locator=self.sales_form, timeout=timedelta(seconds=12))
        if self.browser.does_page_contain_element(self.sales_form):
            logger.info("Logged-In successfully.")
            return True

    def download(self):
        logger.info("downloading file")
        self.http.download(url=self.sales_file_url, overwrite=True,
                           target_file=f"{self.downloading_path}/SalesData.xlsx")

    def sheet(self):
        logger.info("reading sheet.")
        self.file.open_workbook(f'{self.downloading_path}/SalesData.xlsx')
        self.sheet_data = self.file.read_worksheet_as_table(name='data', header=True)
        self.file.close_workbook()

    def form_entries(self):
        try:
            logger.info("making data entries.")
            for data in self.sheet_data:
                if data['First Name']:
                    self.browser.wait_until_page_contains_element(self.form_first_name, timeout=timedelta(seconds=15))
                    self.browser.input_text_when_element_is_visible(self.form_first_name, text=data['First Name'])
                    self.browser.input_text_when_element_is_visible(self.form_last_name, text=data['Last Name'])
                    self.browser.select_from_list_by_value(self.form_sales_target, str(data['Sales Target']))
                    self.browser.input_text_when_element_is_visible(self.form_sales_result, text=str(data['Sales']))
                    self.browser.click_button(locator=self.generic_button)
                    self.sales_entries += 1
            else:
                logger.info(f"{self.sales_entries} entries entered successfully.")
        except Exception as error:
            raise error

    def take_summary_screenshot(self):
        logger.info("taking summary's screenshot...")
        self.browser.wait_until_page_contains_element(self.sales_summary)
        self.browser.screenshot(self.sales_summary, filename=F"{self.downloading_path}/sales_summary.png")

    def result_into_pdf(self):
        logger.info("converting to pdf")
        self.browser.wait_until_page_contains_element(self.sales_result)
        sales_result_html = self.browser.get_element_attribute(self.sales_result, attribute='innerHTML')
        self.pdf.html_to_pdf(sales_result_html, f"{self.downloading_path}/sales_results.pdf")

    def logout(self):
        logger.warning("logging out")
        self.browser.click_button_when_visible(locator=self.logout_locator)

    def close_browser(self):
        logger.warning("closing the browser.")
        self.browser.close_browser()

    def start(self):
        logger.info("Initiating Web bot process....")
        self.open_browser()
        self.login()
        self.download()
        self.sheet()
        self.form_entries()
        self.take_summary_screenshot()
        self.result_into_pdf()

    def finish(self):
        logger.warning("Releasing the resources....")
        self.logout()
        self.close_browser()
