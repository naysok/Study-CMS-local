##

import csv

with open("171222-CSV.csv", newline ="") as f:
    DataReader = csv.reader(f);

    # 最初の行を header として使うときに読み飛ばす
    ## header = next(DataReader) # header を読み飛ばしたい時

    for row in DataReader:
        print(row) # 1行ずつ取得