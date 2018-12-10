seq = [4, 3, 2, 1, 3, 5, 6,]
def add_three(x):
    return x + 3
mapper = map(add_three, seq)
print(list(mapper))

def bounder(x, upper, lower):
    if x > upper:
        return False
    elif x < lower:
        return False
    else:
        return True

#filterer = filter(bounder(, 5, 2), seq)
#print(list(filterer))

seqq = [-4, -2, 0, 1, 3]
def fn(x):
    return (x * x)

print([fn(i) for i in seqq if ((i > 0) and (fn(i) < 5))])
