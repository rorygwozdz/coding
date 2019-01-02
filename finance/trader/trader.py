"""Trader practice thing."""
from mental_math.mather import math_test
from news.newser import updater as news_test
from question_asker import qs
from meditations.bigm import bigm
#  For datekeeping and timing
from datetime import datetime
import csv

# Starting block
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
todays_data = {}
print("Hey! It's {}.".format(today))

# Meditations Portion
print("Let's start with meditations.")
marcus = bigm(json_path='meditations/meditations.json',
                        csv_path='meditations/bigm.csv')
marcus.v()

# Math Portion
print('On to some mental math.')
print("How many math rounds you wanna play?")
math_rounds = int(input())
print("What mode? o, +, or *.")
mode = input()
math_portion = math_test(mode=mode, rounds=math_rounds)
starttime = datetime.now()
amount_wrong = math_portion.play()
endtime = datetime.now()
t_in_secs = (endtime - starttime).seconds
print('Doing {} problems took you {} seconds. Average time per problem was {}\
 seconds.'.format(math_rounds, t_in_secs, t_in_secs/math_rounds))

# News Portion
print("Let's do some news reading. Take ten before you do this.")
news_test(today, filepath='csvs/news.csv').play()

# Probability Portion
print("How many probability rounds you wanna play?")
prob_rounds = input()
qs(filepath='prob_qs/prob_questions.csv', rounds=prob_rounds).play()

# Finance Portion
print("How many finance rounds you wanna play?")
fin_rounds = input()
qs(filepath='fin_qs/finance_questions.csv', rounds=fin_rounds).play()

# Writing math scores to csv
labels = ['date', 'rounds', 'num_wrong', 't_in_secs', 'avg_time_per_round']
data = [today, math_rounds, amount_wrong, t_in_secs, t_in_secs/math_rounds]
for i in range(len(labels)):
    todays_data[labels[i]] = data[i]

with open('csvs/log.csv', 'a') as logg:
    f_names = labels
    writer = csv.DictWriter(logg, fieldnames=labels)
    # Only use if making new log
    writer.writeheader()
    writer.writerow(todays_data)

logg.close()
