import csv 

def writecsv(data):
    # 'a' = append/ 'w' = write or เริ่มเขียน file ใหม่หมด มักใช้กับ export file
    #with open('knowledge.csv','a', encoding='utf-8') as file: 
    with open('knowlendge.csv','a', newline='', encoding='utf-8') as file:    #<---add "newline=''"  เพื่อให้เพิ่มบรรทัดใหม่
        fw = csv.writer(file)   #FW = File Writer

        #ex. data 1 row, data = ['John', 14, 500]  #ความหมายคือ Name, age, money
        fw.writerow(data)   #writerow = write 1 row, writerows= write N row

        #PS. "with open... " -->>>   AUTO close file 


#สร้างข้อมูล
d = ['John', 14, 50] 
# d = ['Robert', 14, 100] 
# d = ['Lisa', 14, 200] 
print(type(d))
writecsv(d)


#ในการรัน ไม่ต้องมี file 'knowlendge.csv' เดียวมันสร้างให้เอง