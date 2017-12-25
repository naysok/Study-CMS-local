import pandas as pd

a = 4


data = pd.read_csv("171222-CSV.csv", header = None)

print("name is "+ data[1][a])

f = open("index.html", "w") # write mode

f.write("<h1>「"+data[0][a]+"」</h1>")
f.write("<h2>"+data[1][a]+"</h2>")
f.write("<hr>")
f.write("<h3>"+data[2][a]+"</h3>")
f.write("<h4>"+data[3][a]+"</h4>")
f.write("<h5>"+data[4][a]+"</h5>")
f.write("<p>"+data[5][a]+"</p>")






f.close() # ファイルを閉じる