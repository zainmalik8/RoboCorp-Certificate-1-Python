import logging
from colorlog import ColoredFormatter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

LOGGER_FORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s {%(filename)s:%(lineno)s - %(funcName)s}" \
                " %(message)s%(reset)s"

stream = logging.StreamHandler()
stream.setFormatter(ColoredFormatter(LOGGER_FORMAT))
logger.addHandler(stream)

if __name__ == '__main__':
    logger.debug("A quirky message only developers care about")
    logger.info("Curious users might want to know this")
    logger.warning("Something is wrong and any user should be informed")
    logger.error("Serious stuff, this is red for a reason")
    logger.critical("OH NO everything is on fire")
