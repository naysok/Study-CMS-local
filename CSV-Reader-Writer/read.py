import pandas as pd

data = pd.read_csv("171222-CSV.csv", header= None)
# print(data) # all

print(data[0][0])
print(data[1][1])
#print(data[1],[3])