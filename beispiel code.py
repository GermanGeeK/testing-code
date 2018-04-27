import pandas as pd
import numpy as np

#1 import von csvs
data = pd.read_csv('Bsp. Datenset.csv', delimiter = ';', low_memory = False)

#2 NaN einfügen
data.replace('k.A.', np.nan, inplace = True)

perso = data['Kandidat']
person = pd.DataFrame(perso)
print(person.dtypes)

number = str(['K1', 'K2', 'K3', 'K4'])
for i in person.iteritems():
    if i == any(number):
        print('richtig')
    else:
        print('falsch')
