from zero_shot_prediction import helper
from zero_shot_prediction import model
import os

config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
CONFIG = helper.load_yaml_file(config_path)
LOGGER = helper.setup_logger()

def run_analysis(data_file=CONFIG['example_data'], model_name = "sentiment_model"):
    """
    Uses sentiment analysis object
    """
        
    LOGGER.info("Analyzing with {}...".format(model_name))
    model_obj = model.Zero_Shot_Model(model_config = CONFIG[model_name], 
                                      data_file = data_file,
                                      logger=LOGGER)
    model_obj.analyze()
    LOGGER.info("{} prediction is finished.".format(model_name))




