import pandas_datareader as web
from datetime import datetime as dt
import matplotlib.pyplot as plt
from datetime import timedelta as td
from hyperparams import Hyperperams as hp

# Get the daily data from a specific Stock
df = web.DataReader(hp.symbol, hp.timeseries, api_key=hp.key)
df = df.reset_index()[hp.index]


# Show the last 130 days so we can compare the outcome of the LSTM with the real data
today = dt.today()
pastdays = 130
pastList = []

for x in range(0, pastdays):
    pastList.append(today - td(days=x))


# Invert the Dates of the past 130 Days for correct plotting
pastList = pastList[::-1]
df = df.tail(pastdays)

# For saving the Graph with actual Date and Time
now = dt.now()
now = now.strftime("%d-%b-%Y_%H-%M-%S")

# Plot the predictet values into a graph
plt.plot(pastList, df, label='Stock Price')
plt.title('Real Stock price of the last 130 Days\nFor ' + hp.stock + ' stock (daily)')
plt.ylabel('Stock price\nin ' + hp.currency)
plt.legend()
plt.xticks(rotation=45)
# Save Predicted Stock price Graph
plt.savefig('graphs/' + hp.stock + '_' + now + '.jpg', bbox_inches='tight', dpi=100)
plt.show()
