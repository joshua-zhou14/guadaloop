import pandas as pd

data = pd.read_csv('data.csv')
cols = list(pd.read_csv("data.csv", nrows=1))

print(data.info())

list = []
#Cleaning the dataset, checking for only the origins/destinations that include Texas (48)
for x in data.index:
    if x == 0:
        continue
    if data.loc[x, "dms_destst"] != 48 or data.loc[x, "dms_origst"] != 48:
        list.append(x)

cols = [i for i in cols if i != "fr_dest" and i != "fr_orig" and i != "fr_inmode" and i!= "fr_outmode"]
data = pd.read_csv('data.csv', skiprows=list, usecols=cols)
print(data.info())

data.to_csv('data.csv', encoding='utf-8', index=False)