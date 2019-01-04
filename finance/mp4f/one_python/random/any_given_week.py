import pandas as pd
import numpy as np
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as pdr
from datetime import datetime

start = datetime(2015, 2, 9)

end = datetime(2018, 5, 24)

def grab_data(ticker, start, end):
    derka = pdr.DataReader(ticker, 'iex', start, end)
    return derka

def weekly_chance_above(derka):
    #need to know how much data
    lengther = len(derka.close)
    #need to have a list to add truthiness
    lister = []
    #need the list to be properly indexable hence the minus five
    for i in np.arange(lengther - 5):
        #if close is higher five days later that's good for me + I buy at open so that's also important
        if derka.open[i] < derka.close[i+5]:
            lister += [True]
        else:
            lister += [False]
    return sum(lister)/len(lister)


def weekly_chance_list(tickers, start, end):
    lister = []
    for i in tickers:
        derka = grab_data(i, start, end)
        chance = weekly_chance_above(derka)
        lister += [i, chance]
    return lister

tickers = ['AAPL','ABBV','ABT','ACN','AGN','AIG','ALL','AMGN','AMZN','AXP','BA','BAC','BIIB','BK','BKNG','BLK','BMY','BRK.B','C','CAT','CELG','CHTR','CL','CMCSA',
'COF','COP','COST','CSCO','CVS','CVX','DHR','DIS','DUK','DWDP','EMR','EXC','F','FB','FDX','FOX','FOXA','GD','GE','GILD','GM','GOOG','GOOGL','GS','HAL',
'HD','HON','IBM','INTC','JNJ','JPM','KHC','KMI','KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MRK','MS','MSFT','NEE','NFLX','NKE',
'NVDA','ORCL','OXY','PEP','PFE','PG','PM','PYPL','QCOM','RTN','SBUX','SLB','SO','SPG','T','TGT','TXN','UNH','UNP','UPS','USB','UTX','V','VZ','WBA',
'WFC','WMT','XOM']

derka = weekly_chance_list(tickers, start, end)

tickers, nums = [], []
for i in range(len(derka)):
    tickers += [derka[i][0]]
    nums += [derka[i][1]]

intial = pd.DataFrame({"ticker": tickers,
                         "chance": nums})

intial = derka_df.sort_values("chance", ascending = False)

## NOTE: The next part of this project is calcualting standard deviations and returns for all of these stocks,
# this way we can see high vol and high chance stocks (i.e. better premiumum)
