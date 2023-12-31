import os
import sys
from transformers import AutoModelForSequenceClassification
from transformers import pipeline
import json
from zero_shot_prediction import helper

PATH = os.path.join(os.path.dirname(__file__))
CONFIG = helper.load_ini_file(os.path.join(PATH, 'config', 'config.ini'))

class Zero_Shot_Model:
    def __init__(self, model_name, data_file, logger):
        """
        Zero shot intent prediction using pretrained Huggingface model
        """
        self.model_name = CONFIG.get(model_name, 'name')
        self.model_path = CONFIG.get(model_name, 'save_model_path')
        self.results_path = CONFIG.get(model_name, 'results_path')
        self.labels = CONFIG.get(model_name, 'intents')
        self.data_file = data_file
        self.data_file_name = data_file.split("/")[-1]
        self.logger = logger
        self.result_dict = {}
        self._save_model_if_not_exists()
        self._load_model()

    def _save_model_if_not_exists(self):
        """
        Save the pretrained model if it does not exist in the save path already
        """

        file_name = os.path.join(self.model_path, self.model_name)

        if not os.path.exists(file_name):
            helper.create_dir_if_not_exists(os.path.join(PATH, self.model_path))
            model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
            model.save_pretrained(os.path.join(PATH, file_name))

    def _load_model(self):
        """
        Loads a trained model from disk into memory and returns an instance of it
        """
        self.model = pipeline("zero-shot-classification", model=self.model_name)

    def _load_data(self):

        if self.data_file == "example_data":
            data = json.load(open(os.path.join(PATH, CONFIG.get(self.data_file, 'default'))))
        else:
            try:
                data = json.load(open(self.data_file))
            except:
                self.logger.error("Data file is not avaliable!")
                raise Exception("Data file is not avaliable!")
        return data

    def _save_results(self):
        """
        Save results as json file
        """

        helper.create_dir_if_not_exists(self.results_path)

        with open(os.path.join(self.results_path, self.data_file_name), "w") as file:
            json.dump(self.result_dict, file)

    def analyze(self):
        """
        Run model on each customer's message and save in results
        """
        data = self._load_data()

        for step in data:
            if step["role"]=="customer":
                result = self.model(step["message"], self.labels)
                self.result_dict[step["id"]] = {"message" : step["message"], 
                                                "intent_labels": result["labels"], 
                                                "intent_scores": result["scores"]}

        self._save_results()
    
