import pandas as pd
import numpy as np
import pandas_datareader as pdr


#importing data
derka = pdr.data.DataReader('CSX', 'robinhood')
print(derka.head())
#making the cols floats
listr = list(derka)
del listr[5]
print(listr)
derka[listr] = derka[listr].astype(float)

##making a new vol column
derka['log return'] = np.log(derka['close_price']/derka['close_price'].shift(1))
derka['vol'] = np.sqrt(252)*derka['log return'].rolling(12).std()

#cell 5 for plotting
#%matplotlib inline
#plot(derka['close_price', 'vol'], color = 'red')
