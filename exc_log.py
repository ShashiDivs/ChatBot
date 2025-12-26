
import logging

# class NoQuantityError(Exception):
#     pass

logging.basicConfig(
    filename='excepts.log',
    filemode='w',
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

try:
    logging.info("This is the operation")
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    logging.error(f"Cannot divide by zero!, This cannot be done")