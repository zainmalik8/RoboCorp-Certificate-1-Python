"""Entry point of the web bot."""

from dataclasses import asdict

from config import BotData
from lazy.project import Process


def task_main():
    process = Process(**asdict(BotData()))
    try:
        process.start()
    except Exception as error:
        print(error)
    else:
        process.finish()


if __name__ == "__main__":
    try:
        task_main()
    except Exception as e:
        print(e)
    else:
        print("Web Bot executed successfully.")
