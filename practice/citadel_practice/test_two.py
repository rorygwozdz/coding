#Test 2

import pandas as pd
import numpy as np
def make_dataframe():
    return pd.read_csv('ADM.csv',index_col='Date')

df = make_dataframe()


def get_ma(df, n=9):
    ma_data = df['AdjClose'][0:n]
    ma= np.mean(ma_data)#build a function that computes a moving average of n periods
    #given a dataframe
    return ma



if __name__ == '__main__':
    print(get_ma(df))
#print the moving average here
