# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  distributed-logging
# FileName:     test_demo.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/07/23
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import logging
from distributed_logging import ConcurrentRotatingFileHandler

default_log_file = "test_demo.log"
default_log_level = "INFO"
default_datetime_format = "%Y-%m-%d %H:%M:%S"
default_log_format = ('%(asctime)s - [PID-%(process)d] - [Thread-%(thread)d] - [%(levelname)s] - %(message)s - ' +
                      '<%(funcName)s> - [Line-%(lineno)d] - %(filename)s')

log = logging.getLogger("root")
log.setLevel(default_log_level)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(default_log_level)
console_handler.setFormatter(logging.Formatter(default_log_format, datefmt=default_datetime_format))

# Create file handler
file_handler = ConcurrentRotatingFileHandler(
    filename=default_log_file, max_bytes=1024 * 1024 * 50, backup_count=9, encoding="utf-8"
)
file_handler.setLevel(default_log_level)
file_handler.setFormatter(logging.Formatter(default_log_format, datefmt=default_datetime_format))

# Add handlers to the logger
if not log.handlers:
    log.addHandler(console_handler)
    log.addHandler(file_handler)
else:
    for handler in log.handlers:
        if isinstance(handler, logging.FileHandler):
            log.removeHandler(handler)
    log.addHandler(console_handler)
    log.addHandler(file_handler)

# Ensure that any existing loggers also follow this format
for logger_name in logging.root.manager.loggerDict:
    existing_logger = logging.getLogger(logger_name)
    if not existing_logger.handlers:
        existing_logger.addHandler(console_handler)
        existing_logger.addHandler(file_handler)
    else:
        for handler in existing_logger.handlers:
            handler.setLevel(default_log_level)
            handler.setFormatter(logging.Formatter(default_log_format, datefmt=default_datetime_format))

log.info("111111111")
