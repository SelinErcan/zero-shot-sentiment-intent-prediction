# Zero Shot Sentiment and Intent Prediction with pretrained Huggingface LLM model(s)

## Table of Contents

- [Files](#Files)
- [Build Python Package](#buildpackage)
- [Usage of local package](#usepackage)

## Files

* data: contains example of simulated conversation
* recources: contains Huggingface pretrained model(s)
* src: source code
    * config/config.ini: model configurations
    * data/simulated_conversation_1.json: example of a simulated conversation
    * helper.py: utility functions
    * analyze.py: runs code
    * model.py: model class
* .gitignore
* requirements.txt

## Build Python Package

### Build Enviroment
```bash
pip3 install --upgrade pip
pip3 install -U pip virtualenv
python -m venv env
env\Scripts\activate # On Windows, use this to activate the virtual environment
pip install -r requirements.txt
```

### Prepare python package
```bash
python setup.py sdist bdist_wheel
```

## Usage of local package

### Load package from the local
```bash
pip install -U zero-shot-prediction --find-links {local_package_destination}
```

### How to use
```python 
from zero_shot_prediction import analyze
analyze.run_analysis(data_file = "file_path", model_name = "sentiment_model")
```
#### Package Parameters

| Parameter      | Description                                 | Default Value           | Options                              |
| -------------- | ------------------------------------------- | ----------------------- | ------------------------------------ |
| data_file      | Conversation file to analyze                | None                    | "example_data", external file path   |
| model_name     | Model selection                             | "sentiment_model"       | "sentiment_model", "intent_model"    |


**External conversation data format:**
```json
[
    {
        "id": 1,
        "role": "...",
        "message": "..."
    },
 // More conversation objects
 ]
```           






