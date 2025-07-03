import csv


def readcsv():
    with open('knowlendge2.csv', newline='', encoding='utf-8') as file:    #<---add "newline=''"  เพื่อให้เพิ่มบรรทัดใหม่

        fr = csv.reader(file)
        data = list(fr)
        print(data)



readcsv()