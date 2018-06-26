import pandas as pd
import numpy as np

#1 import von csvs
data = pd.read_csv('Bsp_Datenset_gemergt.csv', delimiter = ';', low_memory = False, encoding = 'ISO-8859-1')
# skiprows=1, header=None


#2 data cleanup
del data['Unnamed: 5']
#data = data.rename(columns={'Kandidat': '1.Kandidat'})
data = data.sort_index(ascending=True)
data = data.fillna(method = 'ffill', inplace = False, axis = 0)
data_nafilled = pd.DataFrame(data=data)
kandi = data_nafilled.iloc[:,0]
kandi = pd.DataFrame(data=kandi)


#3 dummy variablen erstellen
dummy = pd.get_dummies(data_nafilled.iloc[:,1:]) #alles nach Kandidat-Spalte
join = kandi.join(dummy, how='inner')
#join.to_csv('dummy.csv', sep = ';', index = False, encoding = 'ISO-8859-1')


#4 grouing nach Kandidat

####backup, das hier funktioniert
#grouping = join.groupby('Kandidat')
#grouping_2 = grouping.agg([np.sum])
#grouping_2.to_csv('Gruppen.csv', sep = ';', index = True, encoding = 'ISO-8859-1')
####ende backup


grouping = join.groupby('Kandidat')
#input = grouping.iloc[:,:-3]
#input_2 = input.agg([np.sum])
target = grouping['Antwort: ja/nein_j','Antwort: ja/nein_n']
target_2 = grouping.agg([np.mean])
print(grouping.get_group('K2'))
