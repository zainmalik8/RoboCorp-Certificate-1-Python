"""Entry point of the web bot."""

import os
from dataclasses import dataclass, asdict

from dotenv import load_dotenv

from lazy.project import CertificateOne

load_dotenv()


@dataclass
class BotData:
    username: str = os.getenv("username")
    password: str = os.getenv("password")
    sales_file_url: str = os.getenv("file_url")
    output_path: str = f"{os.getcwd()}/output"


def task_main():
    main_course = CertificateOne(**asdict(BotData()))
    try:
        main_course.open_browser()
        main_course.login()
        main_course.download()
        main_course.sheet()
        main_course.form()
        main_course.screenshot()
        main_course.result_into_pdf()
    finally:
        main_course.logout()
        main_course.close_browser()


if __name__ == "__main__":
    try:
        task_main()
    except Exception as e:
        print(e)
    else:
        print("Web Bot run successfully.")
