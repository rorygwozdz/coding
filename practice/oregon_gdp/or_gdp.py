import numpy as np
import pandas as pd
from string import lower
import matplotlib.pyplot as plt

or_gdp = pd.read_csv('/Users/rory/coding/oregon_gdp/data/or_gdp.csv')

#print list(or_gdp['Industry'])
#adding a column for the fun of it, my friend. Check this shit out: Imma make an Ind code odd column!
#the format is df['col_name'] = whatever_you want it to equal ~ if it's an array, make sure you add it as an array,
# not an array of an arry, if that makes sense i.e. if output of test == array, place just the test
#just remeainder divide by two, it makes ur life easier
#or_gdp['IndCode odd?'] = or_gdp['IndCode']%2 == 1


#you can add really simple things too - like is this true/false?
#or_gdp['In Oregon'] = True

#and you can add based on itemwise column operations(I thuink that's the technical term, anyway
or_gdp['2018:Q2 Prediction'] = np.round(or_gdp['2018:Q1']*(or_gdp['2017:Q2']/or_gdp['2017:Q1']), 1)
or_gdp['2018:Q2 Prediction'].head()
#print or_gdp[-4:-1]

#you can also add functions to the data from by using *gasps* apply
or_gdp['Industry'] = or_gdp['Industry'].apply(lower)
#print or_gdp['Industry']

#and nowwwwww we've got some lambda's to look at it. These are useful for simple addition
#in this case, let's say we forget to account for santa's 11 presents to every industdry in or_gdp
santa = lambda x: x + 11
or_gdp['2018:Q2 Prediction'] = santa(or_gdp['2018:Q2 Prediction'] )
or_gdp['2018:Q2 Prediction'].head()

#and lambda's can have else functions # toooooooo
cool_check = lambda x: "cool" \
    if (or_gdp['Industry'][x] == 0 or 15 or 17) else 'not cool'
def industry_cool(index):
    return "Oregon's %s industry is %s." % (or_gdp['Industry'][index], cool_check(index))

#now, if I want to make a new column to check whether industries are cool, I can do that aswell
print or_gdp.Industry.apply(cool_check)
#or_gdp['Cool Industry'] = or_gdp.Industry.apply(cool_check)
