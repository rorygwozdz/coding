import pandas as pd
import numpy as np
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as pdr
from datetime import datetime




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
    #so this is broken up to allow for creating a "big daddy" dictionary of dataframes.
    #the first lister value is just the first of the tickers and the chance of that ticker
    #the rest of the for loop iterates over the rest of the tickers
    #lister = [[tickers[0], weekly_chance_above(grab_data(tickers[0], start, end))]]
    #big_derka = {tickers[0]: grab_data(tickers[0], start, end)}
    counter, lister, big_derka = 0, [], {}
    for i in tickers:
        indexer= range(len(tickers[1:]))
        derka = grab_data(i, start, end)
        big_derka[tickers[counter]] = derka
        chance = weekly_chance_above(derka)
        lister += [[i, chance]]
        counter += 1
    return big_derka, lister

def expected_value_trade(df, ticker, credit, max_loss):
    chancer = df[df.ticker == ticker].chance
    gain = chancer * credit
    loss = max_loss * (1 - chancer)
    return gain + loss

def corr_getter(df, ticker_1, ticker_2):
    priced_ticker_1 = 0
    priced_ticker_2 = df[df.ti]
    #i need to figure out how to call the column with the syntac I gave it
    #I essentially just need the two price datas ( i think i'll take the close data, too)
    return np.corr(df.tickers)

def make_chancer(lister):
    #returns a df of the chances by ticker
    tickers, nums = [], []
    for i in range(len(lister)):
        tickers += [lister[i][0]]
        nums += [lister[i][1]]
    derka_df = pd.DataFrame({"ticker": tickers,
                         "chance": nums})
    derka_df = derka_df.sort_values("chance", ascending = False)
    return derka_df
