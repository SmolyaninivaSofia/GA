import pandas as pd
data_file='32.txt'
param=pd.read_csv(data_file,sep=" ",encoding='latin1',names=["weight", "voluem", "price"])
wc=param.iloc[0][0]
vc=param.iloc[0][1]
param=param.drop([0])
items=[]
for i in range(0,30):
    items.append([i,param.iloc[i][0],param.iloc[i][1],param.iloc[i][2]])
