from logging import Logger, Formatter, getLogger, DEBUG, StreamHandler, INFO

from app.backend.settings import settings


class Loggers:
    base_logger: Logger = None
    base_formatter: Formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def __init__(self):
        if not self.__class__.base_logger:
            self.__class__.base_logger = self.get_base_logger()

    def get_base_logger(self):
        logger = getLogger('base_logger')
        logging_level = DEBUG if settings.DEBUG else INFO

        logger.setLevel(logging_level)
        console_handler = StreamHandler()
        console_handler.setLevel(logging_level)
        console_handler.setFormatter(self.base_formatter)
        logger.addHandler(StreamHandler())

        return logger
