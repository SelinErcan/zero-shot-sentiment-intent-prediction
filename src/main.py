import helper
import sentiment_analysis
import intent_prediction

CONFIG = helper.load_yaml_file('config/config.yaml')
LOGGER = helper.setup_logger()

def run_sentiment_analysis():
    """
    Uses sentiment analysis object
    """

    LOGGER.info("Analyzing Sentiments...")
    sentiment_obj = sentiment_analysis.SentimentAnalysis(model_config = CONFIG['sentiment_model'], 
                                                          data_file = CONFIG['conversation_data'])
    sentiment_obj.analyze()
    LOGGER.info("Sentiment prediction is finished.")

def run_intent_prediction():
    """
    Uses intent prediction object
    """

    LOGGER.info("Analyzing Intents...")
    intent_obj = intent_prediction.IntentPrediction(model_config = CONFIG['intent_model'],
                                                     data_file = CONFIG['conversation_data'])
    intent_obj.analyze()
    LOGGER.info("Intent prediction is finished.")


if __name__ == "__main__":

    run_sentiment_analysis()
    run_intent_prediction()

