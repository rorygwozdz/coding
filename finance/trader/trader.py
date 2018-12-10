from mental_math.mather import *
from datetime import datetime #for datekeeping and timing
import numpy as np
import csv

#starting block
today = datetime.now().date()
todays_data = {}
print("Hey! It's {}. Let's start with mental math.".format(today))


rounds = 5
# assert rounds > 1
mathh = math_test(rounds)
starttime = datetime.now()
amount_wrong = mathh.play()
endtime = datetime.now()
t_in_secs = (endtime - starttime).seconds
print('Doing {} problems took you {} seconds. Average time per problem was {} seconds.'\
.format(rounds, t_in_secs, t_in_secs/rounds))

#writing to csv
labels = ['date', 'rounds', 'num_wrong', 't_in_secs', 'avg_time_per_round']
data = [today, rounds, amount_wrong, t_in_secs, t_in_secs/rounds]
for i in range(len(labels)):
    todays_data[labels[i]] = data[i]

with open('log.csv', 'a') as logg:
    f_names = labels
    writer = csv.DictWriter(logg, fieldnames = labels)
    writer.writeheader() #only use if making new log
    writer.writerow(todays_data)

logg.close()
