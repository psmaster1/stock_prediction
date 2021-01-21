import math
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime as dt
from datetime import timedelta as td
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM
from hyperparams import Hyperperams as hp


# Get the daily data from a specific Stock
df = web.DataReader(hp.symbol, hp.timeseries, api_key=hp.key)

# Show the first Lines of Data to check if it works
print(df.tail())

# Save the Data into an .csv file to avoid running out of free api requests during programming
#    df.to_csv('AAPL.csv')
# Open the .csv File with pandas an work with it
#    df = pd.read_csv('AAPL.csv')

# seperate the close price of the Stock
prices = df.reset_index()[hp.index]
# show how much closing prices are in the dataset
# print(df1.shape)

# seperate the dates for showing in the graph
date = df.reset_index()['index']
date = np.asarray(date)
dates = []
for row in date:
    dates.append(mdates.date2num(dt.strptime(row, '%Y-%m-%d')))

# save the actual Datetime
now = dt.now()
now = now.strftime("%d-%b-%Y_%H-%M-%S")

# plot the closing prices graph
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.plot(dates, prices)
plt.title('Intraday Chart for the ' + hp.stock + ' stock (daily)')
plt.ylabel('Stock price\nin ' + hp.currency)
plt.xticks(rotation=45)
plt.savefig('graphs/' + hp.stock + '_' + now + '.jpg', bbox_inches='tight', dpi=100)
plt.show()


# Preparing the Data for the LSTM Model
# MinMax scaler will give us an output between 0 and 1
scaler = MinMaxScaler(feature_range=(0, 1))
prices = scaler.fit_transform(np.array(prices).reshape(-1, 1))

# Splitt the Data into Train(65%) and Test(35%)
training_size = int(len(prices) * hp.for_training)
test_size = len(prices) - training_size
train_data, test_data = prices[0:training_size:], prices[training_size:len(prices), :1]


# convert an array of values into a dataset matrix
def create_dataset(dataset, time_step=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step), 0]
        dataX.append(a)
        dataY.append(dataset[i + time_step, 0])
    return np.array(dataX), np.array(dataY)


# reshape into X=t, t+1, t+2, t+3 Y=t+4
time_step = 100
X_train, Y_train = create_dataset(train_data, time_step)
X_test, Y_test = create_dataset(test_data, time_step)

# reshape again so input data becomes three dimensional [samples, time steps, features]
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)


# Create the Model (LSTM)
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(100, 1)))
model.add(LSTM(50, return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')


# Overview of the Model which show how much trainable Layers there are
model.summary()

# Pass the Data into the Model and start training
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=hp.epochs, batch_size=hp.batch_size, verbose=1)

# Do the prediction and check performance
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Transform the given Data back to original
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)


# See how close we get to the closing prices of the test data (RMSE)
print(math.sqrt(mean_squared_error(Y_train, train_predict)))
# If these two numbers are close together, than the training was successful.
# If not, maybe more epochs or another batch_size during training would help.
print(math.sqrt(mean_squared_error(Y_test, test_predict)))


# Shift train prediction for plotting
look_back = 100
trainPredictPlot = np.empty_like(prices)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(train_predict)+look_back, :] = train_predict

# Shift test prediction for plotting
testPredictPlot = np.empty_like(prices)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(train_predict)+(look_back*2)+1:len(prices) - 1, :] = test_predict

# Get actual datetime
now = dt.now()
now = now.strftime("%d-%b-%Y_%H-%M-%S")

# Plot baseline and training-test data
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.plot(dates, scaler.inverse_transform(prices), label='Original Chart')
plt.plot(dates, trainPredictPlot, label='Training Data')
plt.plot(dates, testPredictPlot, label='Predicted Test Data')
plt.title('Training performance for the ' + hp.stock + ' stock (daily)')
plt.ylabel('Stock price\nin ' + hp.currency)
plt.xticks(rotation=45)
plt.legend()
plt.savefig('graphs/' + hp.stock + '_' + now + '.jpg', bbox_inches='tight', dpi=100)
plt.show()


# Predict the future 30 days
# take the past 100 days data for predicting
x_input = test_data[len(test_data)-100:].reshape(1, -1)
# convert it into a list
temp_input = list(x_input)
temp_input = temp_input[0].tolist()
# predict each single day for the next 30 days
lst_output = []
n_steps = 100
i = 0

while i < 30:
    if len(temp_input) > 100:
        x_input = np.array(temp_input[1:])
        x_input = x_input.reshape(1, -1)
        x_input = x_input.reshape((1, n_steps, 1))
        # print(x_input)
        yhat = model.predict(x_input, verbose=0)
        # print("{} day output {}".format(i, yhat))
        temp_input.extend(yhat[0].tolist())
        temp_input = temp_input[1:]
        # print(temp_input)
        lst_output.extend(yhat.tolist())
        i = i + 1
    else:
        x_input = x_input.reshape((1, n_steps, 1))
        yhat = model.predict(x_input, verbose=0)
        # print(yhat[0])
        temp_input.extend(yhat[0].tolist())
        # print(len(temp_input))
        lst_output.extend(yhat.tolist())
        i = i + 1

# print(lst_output)


# Get the Dates of the past 100 and the next 30 Days
today = dt.today()
pastdays = 100
pastList = []

for x in range(0, pastdays):
    pastList.append(today - td(days=x))

futuredays = 30
futureList = []

for y in range(0, futuredays):
    futureList.append(today + td(days=y))

# Invert the Dates of the past 100 Days for correct plotting
pastList = pastList[::-1]

# For saving the Graph with actual Date and Time
now = dt.now()
now = now.strftime("%d-%b-%Y_%H-%M-%S")

# Plot the predictet values into a graph
plt.plot(pastList, scaler.inverse_transform(prices[len(prices) - pastdays:]), label='Past Stock Price')
plt.plot(futureList, scaler.inverse_transform(lst_output), label='Predicted Stock Price')
plt.title('Prediction for the next 30 Days\nFor ' + hp.stock + ' stock (daily)')
plt.ylabel('Stock price\nin ' + hp.currency)
plt.legend()
plt.xticks(rotation=45)
# Save Predicted Stock price Graph
plt.savefig('graphs/' + hp.stock + '_' + now + '.jpg', bbox_inches='tight', dpi=100)
plt.show()