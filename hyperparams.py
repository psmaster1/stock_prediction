class Hyperperams:
    # API Key from AlphaVantage
    key = 'YOUR_API_KEY_HERE'

    # Which Timeseries?
    timeseries = "av-daily-adjusted"
    # Possible Values:
    # av-intraday, av-daily, av-daily-adjusted, av-weekly, av-weekly-adjusted,
    # av-monthly, av-monthly-adjusted, av-forex-daily

    # Which Index from the Data do you want to seperate?
    index = 'close'

    # How much training Data in percent? 0.65 means 65%
    for_training = 0.65

    # Which Stock?
    stock_name = 'Coca-Cola'

    # LSTM Parameters
    epochs = 100
    batch_size = 64

    # Stocks from DAX
    if stock_name == 'SAP':
        stock = stock_name
        symbol = 'SAP.DEX'
        currency = 'EURO'
    elif stock_name == 'Adidas':
        stock = stock_name
        symbol = 'ADS.DEX'
        currency = 'Euro'
    elif stock_name == 'Allianz':
        stock = stock_name
        symbol = 'ALV.DEX'
        currency = 'Euro'
    elif stock_name == 'BASF':
        stock = stock_name
        symbol = 'BAS.DEX'
        currency = 'Euro'
    elif stock_name == 'Bayer':
        stock = stock_name
        symbol = 'BAYN.DEX'
        currency = 'Euro'
    elif stock_name == 'Beiersdorf':
        stock = stock_name
        symbol = 'BEI.DEX'
        currency = 'Euro'
    elif stock_name == 'BMW':
        stock = stock_name
        symbol = 'BMW.DEX'
        currency = 'Euro'
    elif stock_name == 'Continental':
        stock = stock_name
        symbol = 'CON.DEX'
        currency = 'Euro'
    elif stock_name == 'Covestro':
        stock = stock_name
        symbol = '1COV.DEX'
        currency = 'Euro'
    elif stock_name == 'Daimler':
        stock = stock_name
        symbol = 'DAI.DEX'
        currency = 'Euro'
    elif stock_name == 'Delivery Hero':
        stock = stock_name
        symbol = 'DHER.DEX'
        currency = 'Euro'
    elif stock_name == 'Deutsche Bank':
        stock = stock_name
        symbol = 'DBK.DEX'
        currency = 'Euro'
    elif stock_name == 'Deutsche Börse':
        stock = stock_name
        symbol = 'DB1.DEX'
        currency = 'Euro'
    elif stock_name == 'Deutsche Post':
        stock = stock_name
        symbol = 'DPW.DEX'
        currency = 'Euro'
    elif stock_name == 'Deutsche Telekom':
        stock = stock_name
        symbol = 'DTE.DEX'
        currency = 'Euro'
    elif stock_name == 'Deutsche Wohnen':
        stock = stock_name
        symbol = 'DWNI.DEX'
        currency = 'Euro'
    elif stock_name == 'EON':
        stock = stock_name
        symbol = 'EOAN.DEX'
        currency = 'Euro'
    elif stock_name == 'Fresenius':
        stock = stock_name
        symbol = 'FRE.DEX'
        currency = 'Euro'
    elif stock_name == 'Fresenius Medical Care':
        stock = stock_name
        symbol = 'FME.DEX'
        currency = 'Euro'
    elif stock_name == 'HeidelbergCement':
        stock = stock_name
        symbol = 'HEI.DEX'
        currency = 'Euro'
    elif stock_name == 'Henkel':
        stock = stock_name
        symbol = 'HEN3.DEX'
        currency = 'Euro'
    elif stock_name == 'Infineon':
        stock = stock_name
        symbol = 'IFXA.DEX'
        currency = 'Euro'
    elif stock_name == 'Linde':
        stock = stock_name
        symbol = 'LIN.DEX'
        currency = 'Euro'
    elif stock_name == 'Merck':
        stock = stock_name
        symbol = 'MRK.DEX'
        currency = 'Euro'
    elif stock_name == 'MTU Aero Engines':
        stock = stock_name
        symbol = 'MTX.DEX'
        currency = 'Euro'
    elif stock_name == 'Münchener Rück':
        stock = stock_name
        symbol = 'MUV2.DEX'
        currency = 'Euro'
    elif stock_name == 'RWE':
        stock = stock_name
        symbol = 'RWE.DEX'
        currency = 'Euro'
    elif stock_name == 'Siemens':
        stock = stock_name
        symbol = 'SIE.DEX'
        currency = 'Euro'
    elif stock_name == 'Volkswagen':
        stock = stock_name
        symbol = 'VOW3.DEX'
        currency = 'Euro'
    elif stock_name == 'Vonovia':
        stock = stock_name
        symbol = 'VNA.DEX'
        currency = 'Euro'

    # Stocks from Dow Jones
    elif stock_name == 'Heidelberger Cement':
        stock = stock_name
        symbol = 'AAPL'
        currency = 'US-Dollar'
    elif stock_name == 'Microsoft':
        stock = stock_name
        symbol = 'MSFT'
        currency = 'US-Dollar'
    elif stock_name == 'Alphabet':
        stock = stock_name
        symbol = 'GOOGL'
        currency = 'US-Dollar'
    elif stock_name == 'Amazon':
        stock = stock_name
        symbol = 'AMZN'
        currency = 'US-Dollar'
    elif stock_name == 'Netflix':
        stock = stock_name
        symbol = 'NFLX'
        currency = 'US-Dollar'
    elif stock_name == 'Nvidia':
        stock = stock_name
        symbol = 'NVDA'
        currency = 'US-Dollar'
    elif stock_name == 'Biontech':
        stock = stock_name
        symbol = 'BNTX'
        currency = 'US-Dollar'
    elif stock_name == 'Pfizer':
        stock = stock_name
        symbol = 'PFE'
        currency = 'US-Dollar'
    elif stock_name == '3M':
        stock = stock_name
        symbol = 'MMM'
        currency = 'US-Dollar'
    elif stock_name == 'American Express':
        stock = stock_name
        symbol = 'AXP'
        currency = 'US-Dollar'
    elif stock_name == 'Amgen':
        stock = stock_name
        symbol = 'AMGN'
        currency = 'US-Dollar'
    elif stock_name == 'Boeign':
        stock = stock_name
        symbol = 'BA'
        currency = 'US-Dollar'
    elif stock_name == 'Caterpillar':
        stock = stock_name
        symbol = 'CAT'
        currency = 'US-Dollar'
    elif stock_name == 'Chevron':
        stock = stock_name
        symbol = 'CVX'
        currency = 'US-Dollar'
    elif stock_name == 'Cisco':
        stock = stock_name
        symbol = 'CSCO'
        currency = 'US-Dollar'
    elif stock_name == 'Coca-Cola':
        stock = stock_name
        symbol = 'KO'
        currency = 'US-Dollar'
    elif stock_name == 'Dow':
        stock = stock_name
        symbol = 'DJI'
        currency = 'US-Dollar'
    elif stock_name == 'Goldman Sachs':
        stock = stock_name
        symbol = 'GS'
        currency = 'US-Dollar'
    elif stock_name == 'Home Depot':
        stock = stock_name
        symbol = 'HD'
        currency = 'US-Dollar'
    elif stock_name == 'Honeywell':
        stock = stock_name
        symbol = 'HON'
        currency = 'US-Dollar'
    elif stock_name == 'IBM':
        stock = stock_name
        symbol = 'IBM'
        currency = 'US-Dollar'
    elif stock_name == 'Intel':
        stock = stock_name
        symbol = 'INTC'
        currency = 'US-Dollar'
    elif stock_name == 'Bayer':
        stock = stock_name
        symbol = 'JNJ'
        currency = 'US-Dollar'
    elif stock_name == 'JPMorgen':
        stock = stock_name
        symbol = 'JPM'
        currency = 'US-Dollar'
    elif stock_name == 'McDonalds':
        stock = stock_name
        symbol = 'MCD'
        currency = 'US-Dollar'
    elif stock_name == 'Merck':
        stock = stock_name
        symbol = 'MRK'
        currency = 'US-Dollar'
    elif stock_name == 'Nike':
        stock = stock_name
        symbol = 'NKE'
        currency = 'US-Dollar'
    elif stock_name == 'RWE':
        stock = stock_name
        symbol = 'PG'
        currency = 'US-Dollar'
    elif stock_name == 'Salesforce':
        stock = stock_name
        symbol = 'CRM'
        currency = 'US-Dollar'
    elif stock_name == 'Travelers':
        stock = stock_name
        symbol = 'TRV'
        currency = 'US-Dollar'
    elif stock_name == 'UnitedHealth':
        stock = stock_name
        symbol = 'UNH'
        currency = 'US-Dollar'
    elif stock_name == 'Verizon':
        stock = stock_name
        symbol = 'VZ'
        currency = 'US-Dollar'
    elif stock_name == 'Visa':
        stock = stock_name
        symbol = 'V'
        currency = 'US-Dollar'
    elif stock_name == 'Walgreens':
        stock = stock_name
        symbol = 'WBA'
        currency = 'US-Dollar'
    elif stock_name == 'Walmart':
        stock = stock_name
        symbol = 'WMT'
        currency = 'US-Dollar'
    elif stock_name == 'Walt Disney':
        stock = stock_name
        symbol = 'DIS'
        currency = 'US-Dollar'

    # Some Indices
    elif stock_name == 'Dow Jones':
        stock = stock_name
        symbol = 'DIA'
        currency = 'US-Dollar'
    elif stock_name == 'S&P500':
        stock = stock_name
        symbol = 'SPY'
        currency = 'US-Dollar'
    elif stock_name == 'Russel':
        stock = stock_name
        symbol = 'IWM'
        currency = 'US-Dollar'
    elif stock_name == 'DAX':
        stock = stock_name
        symbol = 'DAX'
        currency = 'EURO'

    # Some more Stocks
    elif stock_name == 'Nestle':
        stock = stock_name
        symbol = 'NSRGF'
        currency = 'US-Dollar'
