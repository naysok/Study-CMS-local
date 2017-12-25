import pandas as pd

data = pd.read_csv("171222-CSV.csv", header = None)
print("[ 全体 ]")
print(data) # all

print("-------------------------")



#print(data[0][0])
#print(data[1][1])

a = 1

# 縦
#print("[ 縦 ]")
#print(data[a][0])
#print(data[a][1])
#print(data[a][2])
#print(data[a][3])

#print("-------------------------")

# 横
print("[ 横 ]")
print(data[0][a])
print(data[1][a])
print(data[2][a])
print(data[3][a])
print(data[4][a])
print(data[5][a])


print("-------------------------")
