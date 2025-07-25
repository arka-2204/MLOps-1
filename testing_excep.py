from src.logger import logging
import sys
from src.custom_exception import CustomException

logger= logging.getLogger(__name__)

def divide_number(a,b):
    try:
        result= a/b
        logger.info(f"Division successful: {result}")
        return result
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise CustomException(e, sys)
    
if __name__ == "__main__":
    try:
        divide_number(10, 0)
    except CustomException as ce:
        logger.error(str(ce))
