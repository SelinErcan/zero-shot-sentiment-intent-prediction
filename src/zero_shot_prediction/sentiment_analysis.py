import os
from transformers import AutoModelForSequenceClassification
from transformers import pipeline
import json
from zero_shot_prediction import helper

PATH = os.path.join(os.path.dirname(__file__))

class SentimentAnalysis:
    def __init__(self, model_config, data_file):
        """
        Zero shot sentiment analysis using pretrained Huggingface model
        """
        self.model_name = model_config["name"]
        self.model_path = model_config["save_model_path"]
        self.results = model_config["results"]
        self.data = json.load(open(os.path.join(PATH, data_file)))
        self.result_dict = {}

        helper.create_dir_if_not_exists(self.model_path)
        self._save_model_if_not_exists()
        
    def _save_model_if_not_exists(self):
        """
        Save the pretrained model if it does not exist in the save path already
        """

        file_name = os.path.join(self.model_path, self.model_name)

        if not os.path.exists(file_name):
            model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
            model.save_pretrained(file_name) 

    def _load_model(self):
        """
        Loads a trained model from disk into memory and returns an instance of it
        """
        self.model = pipeline(model=self.model_name)

    def _save_results(self):
        """
        
        """

        helper.create_dir_if_not_exists(self.results["path"])

        with open(os.path.join(self.results["path"], self.results["file_name"]), "w") as file:
            json.dump(self.result_dict, file)

    def analyze(self):
        """
        
        """

        self._load_model()

        for step in self.data:
            if step["role"]=="customer":
                result = self.model(step["message"])[0]
                self.result_dict[step["id"]] = {"message" : step["message"], 
                                                "sentiment_label": result["label"], 
                                                "sentiment_score": result["score"]}

        self._save_results()
