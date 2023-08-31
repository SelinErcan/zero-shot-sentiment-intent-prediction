# Zero Shot Sentiment and Intent Prediction with pretrained Huggingface LLM models

## Table of Contents

- [Overview](#overview)
- [Build Enviroment](#enviroment)
- [Run](#run)
- [Files](#Files)
- [License](#license)

## Overview 


## Build Enviroment

```bash
pip3 install --upgrade pip
pip3 install -U pip virtualenv
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

# make python package
```bash
python setup.py sdist bdist_wheel
```

# load package from local
```bash
pip install -U zero-shot-prediction --find-links {local_package_estination}
```

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




