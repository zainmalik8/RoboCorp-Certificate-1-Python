"""Entry point of the web bot."""

from dataclasses import asdict

from config import BotData
from lazy.project import Certificate


def task_main():
    certificate = Certificate(**asdict(BotData()))
    try:
        certificate.open_browser()
        certificate.login()
        certificate.download()
        certificate.sheet()
        certificate.form_entries()
        certificate.take_summary_screenshot()
        certificate.result_into_pdf()
    except Exception as error:
        print(error)
    else:
        certificate.logout()
        certificate.close_browser()


if __name__ == "__main__":
    try:
        task_main()
    except Exception as e:
        print(e)
    else:
        print("Web Bot run successfully.")
