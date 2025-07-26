from src.logger import get_logger
import os
import pandas
import yaml
from src.custom_exception import CustomException


logger=get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError (f"file not found")
        with open(file_path,"r") as yaml_file:
            config=yaml.safe_load(yaml_file)
            logger.info("read the yaml file")
            return config
    except Exception as e:
        logger.error("error while loading the file")
        raise CustomException("Faild to load",e)