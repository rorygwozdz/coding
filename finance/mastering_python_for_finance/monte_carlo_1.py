import black_scholes_pricer as bsm
import math
import numpy as np
import scipy.stats as sc

derka_inputs= [100, 105, .2, .05, 1, 'call']
derka = bsm.option(derka_inputs)

m = 50
i = 250000
dt = derka.tte/m
s = np.zeros((m+1, i))
s[0] = derka.stock


for sample in range(1, 1+m):
    z = np.random.standard_normal(i)
    s[sample] = s[sample - 1] * np.exp((derka.rate - .5 *derka.vol ** 2)*(dt) + derka.vol * np.sqrt(dt)*z)

guessed_price = math.exp(-1*derka.rate * derka.tte)*np.sum(np.maximum(s[-1] - derka.strike, 0))/i

print(guessed_price)



derka.get_delta()
print(derka.delta)
print(derka.price)
