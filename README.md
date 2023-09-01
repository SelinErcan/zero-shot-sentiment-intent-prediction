# Zero Shot Sentiment and Intent Prediction with pretrained Huggingface LLM models

## Table of Contents

- [Files](#Files)
- [Build Python Package](#buildpackage)
- [How to Use Package](#usepackage)

## Files

* data: contains simulated conversations
* recources: contains Huggingface pretrained models
* results: models output
* src: source code
    * helper.py
    * main.py
    * intent_orediction.py
    * sentiment_analysis.py
* .gitignore
* config.yaml
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

### Preprare python package
```bash
python setup.py sdist bdist_wheel
```

## Use python package in local

### Load package from local
```bash
pip install -U zero-shot-prediction --find-links {local_package_destination}
```

### How to Use Package
```python 
from zero_shot_prediction import analyze
analyze.run_analysis(data_file = "file_path", model_name = "sentiment_model")
```
#### Package Parameters

| Parameter      | Description                                 | Default Value           | Options                              |
| -------------- | ------------------------------------------- | ----------------------- | ------------------------------------ |
| data_file      | Your API key for authentication.            | an example data to run  | default file, external file          |
| model_name     | Timeout in seconds for API requests.        | "sentiment_model"       | "sentiment_model", "intent_model"    |


**External file data format:**
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






