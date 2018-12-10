empty = ""
for i in np.arange(2, 70):
    row = ""
    j = 2
    while j < i:
        row += ","
        j += 1
    while j < 70:
        row += str(magnitude_difference("between", i, j)[0]) + ","
        j += 1
    empty += row + "\n"
    i += 1

emptyy = ""
for i in np.arange(2, 70):
    row = ""
    j = 2
    while j < i:
        row += ","
        j += 1
    while j < 70:
        row += str(magnitude_difference("between", i, j)[1]) + ","
        j += 1
    emptyy += row + "\n"
    i += 1

with open("avg.csv", "w") as outfile:
    outfile.write(empty)
with open("median.csv", "w") as outfile:
    outfile.write(emptyy)
