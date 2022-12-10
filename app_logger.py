import logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

import json_log_formatter

# Константы для роллинга

FILENAME = 'logs/'
WHEN = 'd'
INTERVAL = 1
BACKUPCOUNT = 10


# Конфигурация логов для сохранения в локальный файл строками
FORMAT = '%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'
DATEFMT = '%Y-%m-%dT%H:%M:%S'

logging.basicConfig(
    format=FORMAT,
    datefmt=DATEFMT,
    level=logging.INFO,
)

handler = TimedRotatingFileHandler(
    FILENAME + '.log',
    when=WHEN,
    interval=INTERVAL,
    backupCount=BACKUPCOUNT
)
formatter = logging.Formatter(
    FORMAT,
    datefmt=DATEFMT
)


# Конфигурация логов для сохранения в локальный файл в формате JSON

class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    'Кастомная конфигурация JSON с логами'
    def json_record(
            self, message: str, extra: dict, record: logging.LogRecord
            ) -> dict:
        extra['date'] = datetime.now()
        extra['system'] = record.name
        extra['subsystem'] = record.funcName
        extra['level'] = record.levelname
        extra['message'] = message

        if record.exc_info:
            extra['traceback'] = self.formatException(record.exc_info)

        return extra


formatter_json = CustomisedJSONFormatter()

json_handler = TimedRotatingFileHandler(
    FILENAME + '.json',
    when=WHEN,
    interval=INTERVAL,
    backupCount=BACKUPCOUNT
)
