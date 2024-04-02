import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
cols = list(pd.read_csv("data.csv", nrows=1))

print(data.info())

list = []
#Cleaning the dataset, checking for only the origins/destinations that include Texas (48)
for x in data.index:
    if x == 0:
        continue
    if (data.loc[x, "dms_destst"] == 48 and data.loc[x, "dms_origst"] == 48) and data.loc[x, "dms_mode"] == 1:
        continue
    list.append(x)

cols = [i for i in cols if i != "fr_dest" and i != "fr_orig" and i != "fr_inmode" and i!= "fr_outmode"]
data = pd.read_csv('data.csv', skiprows=list, usecols=cols)
print(data.info())

# data.to_csv('data.csv', encoding='utf-8', index=False)

tmilekey = ['tmiles_2017', 'tmiles_2018', 'tmiles_2019', 'tmiles_2020', 'tmiles_2021', 'tmiles_2022', 'tmiles_2023',
            'tmiles_2025', 'tmiles_2030', 'tmiles_2035', 'tmiles_2040', 'tmiles_2045', 'tmiles_2050']
tmile = []
for i in range(0, len(tmilekey)):
    tmile.append(0)

tonkey = ['tons_2017', 'tons_2018', 'tons_2019', 'tons_2020', 'tons_2021', 'tons_2022', 'tons_2023',
            'tons_2025', 'tons_2030', 'tons_2035', 'tons_2040', 'tons_2045', 'tons_2050']
tons = []
for i in range(0, len(tonkey)):
    tons.append(0)

dbandlowkey = {1: 1, 2: 100, 3:250, 4:500, 5:750, 6:1000, 7:1500, 8:2001}
dbandhighkey = {1: 99, 2: 249, 3:499, 4:749, 5:999, 6:1499, 7:2000, 8:2001}
distbandlow = 0
distbandhigh = 0

for x in data.index:
    if x == 0:
        continue
    for i in range(0, len(tmilekey)):
        tmile[i] += data.loc[x, tmilekey[i]]
        tons[i] += data.loc[x, tonkey[i]]
    distbandlow += dbandlowkey[data.loc[x,"dist_band"]]
    distbandhigh += dbandhighkey[data.loc[x,"dist_band"]]

print(tmile)
print(tons)
sum = 0
for i in tons:
    sum += i
print(sum)
print("low: " + str(distbandlow) + ", high: " + str(distbandhigh))

