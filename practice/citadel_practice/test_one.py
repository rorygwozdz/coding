#Part 1
import numpy as np
print(np.exp(1))
class Dog():

    def __init__(self, name, homestate):
        self.name = name
        self.tricks = []
        self.treats_eaten = []
        self.homestate = homestate

    def learn_tricks(self, trick):
        self.tricks.append(trick)

    def eat_treat(self, treat):
        self.treats_eaten.append(treat)

spot = Dog("spot", "california")
fido = Dog("fido", "washington")
nate = Dog("nate", "oregon")
#Make a dog named spot, Make a dog named fido
#Teach spot how to sit, and fido how to roll over
spot.learn_tricks("sit")
fido.learn_tricks("roll over")
spot.eat_treat("bacon")
spot.eat_treat("biscut")
spot.eat_treat("cookie")


if __name__ == '__main__':
    print(spot.tricks)
    #print fidos tricks here
    #is this behaving how you expected
    #well now that i've fixed it, yeah. if tricks is an attrivute of the object, then you gotta stae as so, not just some list
