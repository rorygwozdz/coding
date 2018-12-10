
import string
#with is used for opening files, doing something with them, and then closing them
with open('meditations.txt') as text:
    bigm = str(text.read())
    bigm = str(bigm)




print(bigm)







derka = '2018'
kflay = '300'

#you can lead with f' to denote formatting, which is clean as fuck
stringer = f'this is a string in {derka} for {kflay} dollars.'
