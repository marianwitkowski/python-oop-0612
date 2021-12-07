"""
 Logowanie w Pythonie
"""
import logging

log_format = "%(asctime)s:%(levelname)s:%(filename)s:%(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=log_format,
                    #filename="app.log",
                    handlers=[
                      logging.StreamHandler(),
                      logging.FileHandler("app.log")
                    ],
                    datefmt="%Y-%m-%dT%H:%M:%S%z")

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warn message")
logging.error("Error message")
logging.critical("Critical message")
logging.fatal("Fatal message")

try:
    y = 1 / 0
except Exception as exc:
    logging.critical("Nie dziel przez zero", exc_info=True)
