print "Oh!"
import numpy as np
import pandas as pd
print "Derka, derka."

fire = pd.read_csv('/Users/rory/coding/fire/data/fire.csv')

#info() tells you about the columns and what's in em
# fire.info()

#selecting only certain columns. Use two brackets or suffer!
year_size_desc = fire[['FireYear', 'GeneralDesc', 'Size_acres']]


#see the type of structure. Notice that calling one row returns a series, calling two or more returns a dataframe
type(fire.iloc[5])
type(fire.iloc[2:5])

#see all the column names
list(fire)

#selects the last two values, from the thing
fire.iloc[-5:]

#selecting all the fires in 2015
fire[fire.FireYear == 2015]

#selecting all fires where it was Lighting or Arson. Remember to put the individual logic process in parantheses.
#this is so that it can test it with objects, not booleans i.e. (in to out: (test ==) -> object of bools -> compare itemwise for each)
zeus_or_baddies = fire[(fire.GeneralDesc == 'Arson') | (fire.GeneralDesc == 'Lightning')]
zeus_or_baddies

#use this for testing a lot of logic (i.e. "is the value of this column in this list?")
#don't forget isin is a function, so you open parantheses. A list comes in brackets, so you open brackets too
#and you have the whole thing as a boolean, so the outside df is testing against brackets (it's sick)
even_years =fire[fire.FireYear.isin([2006, 2008, 2010, 2012, 2014])]
print even_years.head()

#here's how you reset the indexs
#inplace=True equates this df to the old one and resets the indexes (meaning you're not defining many df's)
#drop=True drops the old index column (which is otherwise saved and looks ugly)
even_years.reset_index(inplace=True, drop=True)
print even_years.head()
