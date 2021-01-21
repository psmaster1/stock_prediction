# Stock prediction LSTM Model
A LSTM Model wich predicts stock prices for the next 30 days

1) Create virtual environment (*optional)

2) Install requirements -> `pip install -r requirements.txt`

3) Go to https://www.alphavantage.co/support/#api-key and get you API Key

4) Go to **Hyperparams.py**, copy paste your API Key into the **"key"** variable. Take all settings and select which Stock you want to predict.

5) run -> `python predict.py` than you'll get the prediction for the next 30 days

6) If you want to compare the prediction with the real outcome you can run -> `python compare.py` after 30 days
