import pandas as pd
import numpy as np

d = pd.date_range('20180204', periods = 60)
er = np.random.rand(60, 4)
ka = np.random.rand(60, 4)

der = pd.DataFrame(er, index = d, columns = list('ABCD'))
dka = pd.DataFrame(ka, index = d, columns = list('WXYZ'))
print der.head(3)

derka = der.merge(dka, on=d)
print derka.head(3)
