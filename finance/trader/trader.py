"""Trader practice thing."""
from mental_math.mather import math_test
from news.newser import updater as news_test
#  For datekeeping and timing
from datetime import datetime
import csv

# Starting block
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
todays_data = {}
print("Hey! It's {}. Let's start with mental math.".format(today))

# Math Portion
print("How many rounds do you wanna play?")
rounds = int(input())
print("What mode? o, +, or *.")
mode = input()
math_portion = math_test(mode=mode, rounds=rounds)
starttime = datetime.now()
amount_wrong = math_portion.play()
endtime = datetime.now()
t_in_secs = (endtime - starttime).seconds
print('Doing {} problems took you {} seconds. Average time per problem was {}\
 seconds.'.format(rounds, t_in_secs, t_in_secs/rounds))

# News Portion
print("Let's do some news reading. Take ten before you do this.")
news_test(today, filepath='csvs/news.csv').play()

# Writing to csv
labels = ['date', 'rounds', 'num_wrong', 't_in_secs', 'avg_time_per_round']
data = [today, rounds, amount_wrong, t_in_secs, t_in_secs/rounds]
for i in range(len(labels)):
    todays_data[labels[i]] = data[i]

with open('csvs/log.csv', 'a') as logg:
    f_names = labels
    writer = csv.DictWriter(logg, fieldnames=labels)
    # Only use if making new log
    writer.writeheader()
    writer.writerow(todays_data)

logg.close()
