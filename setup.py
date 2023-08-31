from setuptools import setup, find_packages

setup(
    name='zero_shot_prediction',
    version='0.1',
    packages=find_packages('src'),
    package_data={'zero_shot_sentiment_intent_prediction': ['config/config.yaml', 'data/simulated_conversation_1.json']},
    package_dir={'': 'src'},
    install_requires=[
        'torch>=1.13.1',
        'transformers>=4.27.2',
        'PyYAML'
    ],
    author='Selin Çiğsem Ercan',
    author_email='cigsemercan@gmail.com',
    description='Zero shot prediction on ChatGPT generated data using Huggingface pretrained models',
    url='https://github.com/SelinErcan/zero-shot-sentiment-intent-prediction',
)
