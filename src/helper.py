import yaml
import os
import logging

def load_yaml_file(file_name):
    """
    Loads yaml files

    return: dict
    """
    with open(file_name, 'r') as f:
        yaml_file = yaml.safe_load(f)
    return yaml_file

def create_dir_if_not_exists(dir_name):
    """
    Creates given directory
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def setup_logger():
    logging.basicConfig(filename="std.log",  format='%(asctime)s %(message)s', filemode='w') 
    logger=logging.getLogger() 
    logger.setLevel(logging.DEBUG) 
    console_handler = logging.StreamHandler() 
    console_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    logger.addHandler(console_handler)
    return logger