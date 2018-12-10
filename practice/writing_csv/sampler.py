import numpy as np
import csv


lister1 = ['john', 'cena']
lister2 = ['K', 'FLAY']
with open('derka.csv', 'w') as csver:
    # np.savetxt(file, np.array(lister), header = 'test', delimiter = ",")
    f_names = ['first', 'last']
    writer = csv.DictWriter(csver, fieldnames = f_names)

    writer.writeheader()
    writer.writerow({f_names[0]:lister1[0], f_names[1]: lister1[1]})
    writer.writerow({f_names[0]:lister2[0], f_names[1]: lister2[1]})
