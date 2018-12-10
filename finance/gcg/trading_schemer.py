import numpy as np
import pandas as pd




class trade():
    def __init__(self, ticker, mp, ml):
        if ticker.upper() in tickers:
            self.ticker =  ticker
        else:
            print("ERROR: We don't have data on that ticker.")
        self.data = pd.read_csv("/Users/rory/coding/finance/gcg/data/chances.csv", delimiter =',')
        self.max_profit = mp
        if ml > 0:
            print("You said the max loss was positive; I switched it to negative.")
            self.max_loss = -1*ml
        else:
            self.max_loss = ml
    def ev_trade(self):
        #so, yeah, this is where the gradient will come in
        chance_above = self.data.chance[self.data.ticker == self.ticker]
        self.chance = chance_above
        self.ev = np.round(self.chance*self.max_profit + (1-self.chance)*self.max_loss, 2)
        return self.ev


print("You trading or what?")
trading = input()
while trading != 'no':
    print("Ticker (can be vxx or whatever):")
    ticker = input()
    ticker = ticker.upper()
    print("Max Profit:")
    mp = float(input())
    print("Max Loss:")
    ml = float(input())
    potential_trade = trade(ticker, mp, ml)
    potential_trade.ev_trade()
    print("The expected value for this %s trade is roughly %s." % (potential_trade.ticker, float(potential_trade.ev)))
    print("You still trading or what?")
    trading = input()
