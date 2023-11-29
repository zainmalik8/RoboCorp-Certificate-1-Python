"""Entry point of the web bot."""

import os
from dataclasses import dataclass, asdict

from dotenv import load_dotenv

from lazy.project import Certificate

load_dotenv()


@dataclass
class BotData:
    username: str = os.getenv("username")
    password: str = os.getenv("password")
    sales_file_url: str = os.getenv("file_url")
    output_path: str = f"{os.getcwd()}/output"


def task_main():
    certificate = Certificate(**asdict(BotData()))
    try:
        certificate.open_browser()
        certificate.login()
        certificate.download()
        certificate.sheet()
        certificate.form()
        certificate.screenshot()
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
