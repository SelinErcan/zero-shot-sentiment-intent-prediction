from zero_shot_prediction import helper
from zero_shot_prediction import sentiment_analysis
from zero_shot_prediction import intent_prediction
import os

config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
CONFIG = helper.load_yaml_file(config_path)
LOGGER = helper.setup_logger()

def run_sentiment_analysis(data_file=CONFIG['example_data']):
    """
    Uses sentiment analysis object
    """

    LOGGER.info("Analyzing Sentiments...")
    sentiment_obj = sentiment_analysis.SentimentAnalysis(model_config = CONFIG['sentiment_model'], 
                                                          data_file = data_file)
    sentiment_obj.analyze()
    LOGGER.info("Sentiment prediction is finished.")

def run_intent_prediction(data_file=CONFIG['example_data']):
    """
    Uses intent prediction object
    """

    LOGGER.info("Analyzing Intents...")
    intent_obj = intent_prediction.IntentPrediction(model_config = CONFIG['intent_model'],
                                                     data_file = data_file)
    intent_obj.analyze()
    LOGGER.info("Intent prediction is finished.")



