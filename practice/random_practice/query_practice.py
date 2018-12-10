import pandas as pd
import numpy as np

df = pd.DataFrame({'closing_price': np.random.randint(95, 105, 100), 'opening_price': np.random.randint(95, 105, 100)})

low_price = 96
high_price = 104
netween = 'cp\'s between %s and %s' %(low_price, high_price), df.query('@low_price <= closing_price <= @high_price').head(3)
outside = 'closing prices outside %s and %s' %(low_price, high_price), df.query(' @high_price <= closing_price or closing_price <= @low_price')
below = 'closing prices above %s' % (high_price), df.query('closing_price >= 102').head(3)
above=  'cp\'s below %s' % (low_price), df.query('98 <= closing_price').head(3)
print outside
