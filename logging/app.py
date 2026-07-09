import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
        ]
)
logger=logging.getLogger("Arithmatic app")
def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result
def subtract(a,b):
    result = a-b
    logger.debug(f"Subtraction {a}-{b}={result}")
    return result
def multiply(a,b):
    result = a*b
    logger.debug(f"Multiplication {a}*{b}={result}")
    return result
def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Division {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(4,9)
subtract(8,4)
multiply(4,5)
divide(9,3)
