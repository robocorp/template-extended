from robot.api import logger

# example of accessing a variable from variables.py
from variables import TODAY


class MyLibrary:
    """Give this library a proper name and document it."""

    def example_python_keyword(self):
        logger.info("This is Python!")
        logger.info(f"... and today is {TODAY}")
