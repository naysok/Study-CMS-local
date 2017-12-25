Study  
Contents Management System  

---  

convert CSV file to HTML  

source : 171106-test.csv  
01.py  

---  

**CSV-Reader-Writer**  
python + Pandas  

src : 171222-CSV.csv  

- read-Pandas.py :  指定したセルで読み出し  
- read-all.py : 全て読み込み  
- read.py : 仮実行ファイル  

- write-basic.py : 書き込みテスト  
- write-from-csv.py :　csv から指定したセルの読み出しから、ファイルに書き込み  
- write.py : 仮実行ファイル  



---  

**img-Resize-sips**  

$ bash Hello.sh  

resize sips  

---  

**Make_html_PDF_To_Cheak_Photo**  

卒制展 web 、アーカイブ用の写真を集めてから、公開前に一覧にして全体に確認必要。  
複数枚の画像と、ファイルの名前をまとめて並べてPDF化、イラレでいちいち作業するのも面倒なのでこれ。  

1. 画像ファイルを連番の名前に変更。  
2. processing の for 繰り返しと、println で、コンソールに文字列出す。それを html で保存。  
3. atom で開く。システムで使う文字と被るので、["]が出せなかった。processing では[y]にしておいて、atom で["]置換。html 上書き保存。  
4. html を chrome で開いて、ファイル>印刷で、PDF 保存。  
5. 軽量化サービスに投げる  

processing じゃなくてもいいので、今度、python に直す  


---  

