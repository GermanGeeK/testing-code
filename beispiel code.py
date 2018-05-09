import pandas as pd
import numpy as np

#1 import von csvs
data = pd.read_csv('Bsp_Datenset_no_nan.csv', delimiter = ';', low_memory = 'False', encoding = 'utf-8')

#2 NaN einfügen und auffüllen
#data.replace('k.A.', np.nan, inplace = True)
#print(data['Kandidat'])
#data['Kandidat'].fillna(method = 'ffill', inplace = True)

#data = data.replace(np.nan, '', regex=True) #wahrscheinlich gar nicht nötig ;)
#data['Kandidat'] = data['Kandidat'].astype(str)


#3 Antwort-Spalte erstellen und füllen
antwort = pd.read_csv('Bsp. Reaktionen.csv', delimiter = ';', low_memory = 'False', encoding = "ISO-8859-1")
antwort_spalte = antwort['Antwort: ja/nein']
K1 = data['Kandidat']
K2 = antwort['Kandidat']
#for i in np.nditer(antwort_spalte, flags = 'REFS_OK'):
for i in antwort_spalte.iterrows():
    if K1.sort_index(inplace = True) == K2.sort_index(inplace = True):
        data['Antwort'] = i

print(data['Antwort'])

#data.to_csv('Bsp_Datenset_no_nan.csv', sep = ';', index = False)