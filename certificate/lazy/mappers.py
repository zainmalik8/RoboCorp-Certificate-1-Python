"""Data Mappers"""


class XpathMapper:
    username_field = "//input[contains(@id, 'name')]"
    password_field = "//input[contains(@id, 'pass')]"
    generic_button = "//button[contains(@class, 'btn-primary')]"

    sales_form = "//form[contains(@id, 'sales')]"

    form_first_name = "//input[contains(@name, 'first')]"
    form_last_name = "//input[contains(@name, 'last')]"
    form_sales_target = "//select[contains(@id, 'sales')]"
    form_sales_result = "//input[contains(@name, 'result')]"

    sales_summary = "//div[contains(@class, 'sales-summary')]"
    sales_result = "//div[contains(@id, 'sales-results')]"

    logout_locator = "//*[contains(text(), 'Log out')]"
