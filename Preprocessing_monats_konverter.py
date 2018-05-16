import pandas as pd
import numpy as np
import re

#1 import von csv
data = pd.read_csv('Bsp. Datenset_UTF_8.csv', delimiter = ',', low_memory = 'False', encoding = 'utf-8')
monats_spalte = data.loc[:,'Dauer']
test_data = pd.DataFrame(monats_spalte)

#2 regex für Monats-Erkennung
dauer_regex_1 = re.compile(r'(\d+\s+(\w{5})+\s+\d+\s+(\w{6}))')
dauer_regex_2 = re.compile(r'(\d+\s+(\w{4})+\s+\d+\s+(\w{5}))')
dauer_regex_3 = re.compile(r'(\d+\s+(\w{4})+\s+\d+\s+(\w{6}))')
dauer_regex_4 = re.compile(r'(\d+\s+(\w{5})+\s+\d+\s+(\w{5}))')
data.Dauer.replace('k.A.', np.nan, inplace = True)

#3 Definiton der Umrechung
def umrechner(x):
    if(re.match(dauer_regex_1, x) or re.match(dauer_regex_2, x) or re.match(dauer_regex_3, x) or re.match(dauer_regex_4, x)):
        t = x.split(' ')
        return int(t[0])*12+int(t[2])
    elif('Jahr' in x):
        t = x.split(' ')
        return int(t[0])*12
    elif('Monat' in x):
        t = x.split(' ')
        return int(t[0])
    else:
        return x

#4 Ausgabe und Speichern
data['Dauer_in_Monaten'] = data['Dauer'].astype(str).apply(lambda x: umrechner(x))
monate = data.loc[:, 'Dauer_in_Monaten']

data.to_csv('Bsp_Datenset_inc_Monaten.csv', sep = ';', index= 'False', encoding = 'utf-8')