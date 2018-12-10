import numpy as np
import pandas as pd

def make_dataframe():
    return pd.read_csv('ADM.csv',index_col='Date')

df = make_dataframe()

class ma():
    def __init__(self):
        self.ma_data = []
        self.ma10 = np.mean(df['AdjClose'][0:9])
        self.ma20 = np.mean(df['AdjClose'][0:19])
        self.ma50 = np.mean(df['AdjClose'][0:49])
        self.ma100 = np.mean(df['AdjClose'][0:99])
    def get_ma_data(self, n):
        self.ma_data = []
        for i in np.arange(x_days_ma):
            ma_for_x_day = np.mean(df['AdjClose'][i:x_days_ma+i])
            self.ma_data.append(ma_for_x_day)
        #build a function that computes a moving average of n periods
        #given a dataframe
amd = ma()
amd.get_ma_data(10)
amd.get_ma_data(100)

print(len(amd.ma_data))
