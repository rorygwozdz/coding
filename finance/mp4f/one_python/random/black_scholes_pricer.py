import numpy as np
import scipy.stats as sc

class option():
    def __init__(self, inputs_array, price = []):
        if len(inputs_array)!= 6:
            print("Your input array should be an array with stock price, strike, vol as a decimal, interest rate as a decimal, time to expo as a decimal fraction of a year, and whether it's a 'put' or 'call'")
            return None
        self.stock = float(inputs_array[0])
        self.strike = float(inputs_array[1])
        self.vol = float(inputs_array[2])
        self.rate = float(inputs_array[3])
        self.tte = float(inputs_array[4])
        self.type = inputs_array[5]
        self.price = price
        self.delta = []
        self.gamma = []
        self.d1 = []
        self.d2 = []

    def get_price(self):
        e = np.exp(1.)
        d1 = (np.log((self.stock)/(self.strike))+(self.rate+.5*self.vol**2.)*(self.tte))/(self.vol*np.sqrt(self.tte))
        d2 = d1 - self.vol*np.sqrt(self.tte)
        self.d1 = d1
        self.d2 = d2
        if self.type == 'call':
            s = self.stock
            k = self.strike
            nd1 = sc.norm.cdf(d1)
            nd2 = sc.norm.cdf(d2)
            rate_term = -1.*self.rate*self.tte
            price = s*nd1 - k * (e**rate_term) * nd2
            self.price = price
        else:
            s = self.stock
            k = self.strike
            nd1 = sc.norm.cdf(-1. * d1)
            nd2 = sc.norm.cdf(-1. *d2)
            rate_term = -1.*self.rate*self.tte
            price = k * (e** (rate_term)) * nd2 - s * nd1
            self.price = price

    def get_delta(self):
        self.get_price()
        if self.type == 'call':
            self.delta = sc.norm.cdf(self.d1)
        else:
            #needs to be negative because as stock increases by one point,
            #put decreases in value (ceteris paribus)
            self.delta = (sc.norm.cdf(self.d1) - 1)

    def get_gamma(self):
        self.get_price()
        self.gamma = sc.norm.pdf(self.d1)/(self.stock*self.vol*np.sqrt(self.tte))

    def get_vega(self):
        self.get_price()
        #just the math
        vega = self.stock*sc.norm.cdf(self.d1)*np.sqrt(self.tte)
        self.vega = vega

    def get_imp_vol(self, vol_guess, iterations = 100):
        #want to have a static "pegged price" and another price which iterates
        self.vol = vol_guess
        for i in range(iterations):
            self.vol -= ()





sample_call_inputs_1 = [100, 105, .2783, .06, .5, 'call']
sample_call_inputs_2 = [100, 110, .2783, .06, .5, 'call']
sample_call_1 = option(sample_call_inputs_1)
sample_call_2 = option(sample_call_inputs_2)


sample_put_inputs_1 = [100, 105, .2783, .06, .5, 'put']
sample_put_1 = option(sample_put_inputs_1)
sample_put_inputs_2 = [100, 110, .2783, .06, .5, 'put']
sample_put_2 = option(sample_put_inputs_2)


#checks that same strike delta's absolute value sum to one

#print(np.round((abs(sample_put_1.delta) + abs(sample_call_1.delta)), 5) == 1)
#print(np.round((abs(sample_put_2.delta) + abs(sample_call_2.delta)), 5) == 1)
