"""Template robot with Python."""

import os

from lazy.project import CertificateOne
from lazy.open_secret import username, password, file_url

path = F"{os.getcwd()}/output"


def just_run_it():
    main_course = CertificateOne(username=username, password=password, downloading_path=path,
                                 downloading_file=file_url)
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


def minimal_task():
    print("Done.")


if __name__ == "__main__":
    try:
        just_run_it()
    except Exception as e:
        print(e)
    else:
        minimal_task()
