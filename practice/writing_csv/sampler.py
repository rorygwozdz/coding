"""For my own practice for writing CSV's. Applied in Trader.py."""
import csv

lister1 = ['damn', 'right']
lister2 = ['yeah', 'hell']
with open('derka.csv', 'a', newline='') as csver:
    # 'a' means append, 'w' means write, 'r' means read
    # use 'a' for adding to preset csv's and 'w' for making one
    # newline means that the row is written to a new row
    f_names = ['first', 'last']
    writer = csv.DictWriter(csver, fieldnames=f_names)

    # writer.writeheader()
    writer.writerow({f_names[0]: lister1[0], f_names[1]: lister1[1]})
    writer.writerow({f_names[0]: lister2[0], f_names[1]: lister2[1]})
