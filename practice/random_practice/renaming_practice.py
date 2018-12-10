import pandas as pd
import numpy as np
import matplotlib as plt
derka = np.random.randn(21, 4)
derka_dates = pd.date_range('20180611', periods = 21)
first_derkaframe = pd.DataFrame(derka, index=derka_dates, columns = list('IDFC'))
print first_derkaframe
second_derka_frame = first_derkaframe.rename(index=str, columns = {"D": "know kow", "F": "to do", "C": "this"})
print second_derka_frame
