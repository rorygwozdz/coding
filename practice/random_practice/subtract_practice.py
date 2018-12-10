import pandas as pd
import numpy as np

donuts_bought = pd.DataFrame({'index': np.arange(50), 'donuts': np.full(50, 12)})
donuts_consumed = pd.DataFrame({'index': np.arange(50), 'eaten': np.random.randint(0, 12, 50)})

donuts = donuts_bought.merge(donuts_consumed, on = 'index')

new = donuts[['donuts']].sub(donuts['eaten'], axis=0)
print donuts_consumed['eaten']
print new['donuts']
