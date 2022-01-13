"""Template robot with Python."""

import os

from lazy.project import CertificateOne
from lazy.open_secret import username, password, file_url

path = F"{os.getcwd()}/output"
print(path)


def just_run_it():
    try:
        main_course = CertificateOne(username=username, password=password, downloading_path=path,
                                     downloading_file=file_url)
        main_course.download_directory()
        main_course.open_browser()
        main_course.login()
        main_course.download()
        main_course.sheet()
        main_course.form()
        # main_course.press()
    finally:
        "we call logout and close function at the end"


def minimal_task():
    print("Done.")


if __name__ == "__main__":
    just_run_it()

    minimal_task()
