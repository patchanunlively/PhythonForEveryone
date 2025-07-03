import csv

#!!!!!!
#รันต่อจาก file "Ep11-1-GUI-writereadcsv-write.py"


def readcsv():

    #บาง env. จะงง directory อาจต้องใส่ path เต็มให้มัน อาจเริ่มจาก c:\\xxx\\ หรือ mac เช่น //Users/...
    #with open('//Users//Mameng//Documents//TestPython//knowledge.csv', newline='', encoding='utf-8') as file:    #<---add "newline=''"  เพื่อให้เพิ่มบรรทัดใหม่
    with open('knowledge.csv', newline='', encoding='utf-8') as file:    #<---add "newline=''"  เพื่อให้เพิ่มบรรทัดใหม่

        fr = csv.reader(file)
        data = list(fr)
        print(data)

readcsv()



#ในการรัน ไม่ต้องมี file 'knowlendge.csv' เดียวมันสร้างให้เอง