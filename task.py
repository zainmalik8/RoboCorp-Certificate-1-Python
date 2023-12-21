"""Entry point of the web bot."""

from dataclasses import asdict
from logger import logger
from config import BotData
from workflow.project import Process


def task_main():
    process = Process(**asdict(BotData()))
    try:
        process.start()
    except Exception as error:
        logger.error(error)
    else:
        process.finish()


if __name__ == "__main__":
    try:
        task_main()
    except Exception as e:
        logger.error(e)
    else:
        logger.info("Web Bot executed successfully.")
