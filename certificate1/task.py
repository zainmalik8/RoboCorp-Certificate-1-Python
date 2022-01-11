"""Template robot with Python."""

from lazy.project import CertificateOne
from lazy.open_secret import username, password


def just_run_it():
    main_course = CertificateOne(username=username, password=password)
    main_course.open_browser()
    main_course.login()


def minimal_task():
    print("Done.")


if __name__ == "__main__":
    just_run_it()

    minimal_task()
