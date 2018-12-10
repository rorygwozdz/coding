d = 'Oh? '
e = 'Derka, Derka'
phrase_you_say_all_the_time = d + e
print "The phrase you say all the time, ", phrase_you_say_all_the_time," has ", len(phrase_you_say_all_the_time), " characters."

r= 'Derka'
print"You can say ", r.upper(), "by using the .upper() notation on a string and ", r.lower(), "by using the .lower() function."
print'This is good because the orginal string might be not upper or lower case like this orginal variable is i.e', r

#messing around with numbers
k = 69.69
a = int(k - .69)

print "Here's, ", k, " divided by 3:", k/3

print float(a/3)
print int(k/3.2)

print "If you wanna be a little vulgar, and combine some sexy numbers with sexy phrases try concatenation of strings. Like the below ;)"
print e + " " + str(a) +" oooooooh baby ;)"
#essetnitally, combing strings with numbers for cocatenation is easy so long as you use the string method
# also though, with variablse we can do some fun stuff around concatenttion

name = "Mike"
print "Hello %s" % (name)
print "new way to say %s " % (r)
