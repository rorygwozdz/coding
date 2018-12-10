import numpy as np

#spot rate = 100/e**rt where r is the compounding rate <- for all t

class bond():
    risk_free_rate = .031
    def __init__(self, inputs_array):
        if inputs_array[3] in ('zero', 'annual', 'semiannual', 'monthly'):
            self.par = inputs_array[0]
            self.coupon = inputs_array[1]
            self.ttm = inputs_array[2]
            self.payment_type = inputs_array[3]
            if len(inputs_array) == 5:
                self.price = inputs_array[4]
            else:
                self.price = []
        else:
            print("Payment schedule has options: zero, annual, semiannual, monthly. Try those instead of: %s." %(inputs_array[3]))
            return None
    #I'll have to add a type getter, and that's okay
    def get_price(self):
        self.price = []
        if self.payment_type == 'zero':
            new_price = self.par/(1+self.ytm)**self.ttm
            self.price.append(new_price)
            self.price = self.price[0]*100
    def get_rate(self):
        self.rate = np.log(self.par/self.price)/self.ttm



derka = (bond([1., .05, 5, "zero", ]))
derka.get_price()
print(derka.price)
