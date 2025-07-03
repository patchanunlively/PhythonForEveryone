
#---write file-----------------------
import csv 
def writecsv(data):
    csvfile = os.path.join(path,fileNameCsv)
    with open(csvfile,'a', newline='', encoding='utf-8') as file: 
        fw = csv.writer(file)   
        fw.writerow(data)   #writerow = write 1 row, writerows= write N row



#---GUI-----------------------

from tkinter import * 
from tkinter import ttk , messagebox
import csv
import os


def save():
    tit = v_tit.get()
    textbox = T1.get(1.0,"end-1c")  
    print('----------------------')
    print(tit)
    print([textbox])    #print(textbox) 
    print('----------------------') 
    data = [tit, textbox]
    writecsv(data)  # call write file

    #clear data
    v_tit.set('')
    T1.delete('1.0', END) 


#update
# path = os.getcwd() 
# path = os.path.join(path , "Ep12")  
# print('Path = ', path)


#------------------------------------
# ตรวจสอบว่ารันในรูปแบบ executable (PyInstaller) หรือสคริปต์ Python ปกติ
import sys # เพิ่มการ import sys

if getattr(sys, 'frozen', False):
    # ถ้าโปรแกรมถูกรันจาก PyInstaller executable (เช่น .app บน Mac)
    # sys._MEIPASS คือ path ไปยังโฟลเดอร์ชั่วคราวที่ PyInstaller แตกไฟล์ resource ออกมา
    # ถ้า resource (ไฟล์ .csv, .icns, .png) ถูกรวมไว้กับ executable โดย PyInstaller
    # มันจะอยู่ที่นี่
    bundle_dir = sys._MEIPASS
else:
    # ถ้าโปรแกรมรันเป็นสคริปต์ Python ปกติ
    # os.path.dirname(os.path.abspath(__file__)) จะให้ path ของ directory ที่สคริปต์นี้อยู่
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

# กำหนด path หลักที่โปรแกรมจะใช้
# เนื่องจากไฟล์ Ep12.csv, flashcardIconMac.icns, flashcard.png อยู่ใน subfolder 'Ep12'
# หรืออยู่คนละระดับกับตัว executable เราต้องปรับ path ให้ถูกต้อง
# ถ้า Ep12.csv, flashcardIconMac.icns, flashcard.png อยู่ในโฟลเดอร์เดียวกันกับ Ep12-practice executable
# ให้ใช้:
# path = bundle_dir
# แต่จากโครงสร้างที่คุณเคยบอกมาว่า path = os.path.join(path , "Ep12")  
# แสดงว่าคุณต้องการให้ไฟล์ต่างๆ อยู่ในโฟลเดอร์ย่อยชื่อ 'Ep12'
# ดังนั้นเราจะสร้าง path ที่ชี้ไปที่โฟลเดอร์ 'Ep12' ภายใน bundle_dir หรือ directory ที่สคริปต์อยู่
path = os.path.join(bundle_dir, "Ep12") # สร้าง path ใหม่ให้ชี้ไปที่โฟลเดอร์ Ep12

# ตรวจสอบว่าโฟลเดอร์ Ep12 มีอยู่หรือไม่ ถ้าไม่มี ให้สร้างขึ้นมา
if not os.path.exists(path):
    os.makedirs(path)

print('Path = ', path)
#------------------------------------


fileNameCsv = "Ep12-update-path.csv"

flashicon = os.path.join(path, 'flashcardIconMac.icns')



GUI = Tk() #คนอื่นอาจจะเรียกว่า root เราเรียก GUI
GUI.title('โปรแกรมบันทึกความรู้ By Loong-แบบสวยขึ้น')
GUI.geometry('700x700')

GUI.iconbitmap(flashicon) #รูป icon ที่อยู่ตรงชื่อหน้าต่าง mac เหมือนจะไม่แสดงให้ คงต้องลองอย่างอื่น

F1 = Frame(GUI)
F1.place(x=20, y=50)


L1 = ttk.Label(F1, text='Title', font=('Angsana New',18))
L1.pack()

v_tit = StringVar()  
E1 = ttk.Entry(F1, textvariable = v_tit, font=('Angsana New',20),width=50)   #เอาค่าจาก E1 ไปเก็บในตัวแปร v_tit
E1.pack()


L3 = ttk.Label(F1, text='Description', font=('Angsana New',18))
L3.pack()

T1 = Text(F1, font=('Angsana New',18), height = 8, width=56) 
T1.pack()
 

B1 = ttk.Button(F1, text = 'บันทึก', command = save) #ผุกปุ่มหรือcommand กับ function-save 
B1.pack(pady=10, ipadx=20, ipady=10)

#----Flashcard
def readcsv():
    csvfile = os.path.join(path,fileNameCsv)
    with open(csvfile, newline='', encoding='utf-8') as file:    #<---add "newline=''"  เพื่อให้เพิ่มบรรทัดใหม่
        fr = csv.reader(file)
        data = list(fr)
        return data

#knowledgelist = readcsv() #ดึงครั้งเดียวตอนแรก
#print(knowledgelist)

global countindex
countindex = 0

def showScrFlashcard():
    try:
        knowledgelist = readcsv() #ถ้าใส่ตรงนี้จะดึงใหม่ทุกรอบที่กดปุ่มรูปภาพ ถ้าใส่ข้างนอกจะดึงแค่ครั้งแรก
        print(knowledgelist)

        GUI2 = Toplevel()  #สร้างอีกหน้าต่างนึง
        GUI2.title('ทบทวนความรู้')
        GUI2.geometry('500x400')

        v_text_title = StringVar()
        v_text_detail = StringVar()
        title = ttk.Label(GUI2, textvariable=v_text_title)
        title.pack()
        v_text_title.set(knowledgelist[0][0])
        detail = ttk.Label(GUI2, textvariable=v_text_detail)
        detail.pack()
        v_text_detail.set(knowledgelist[0][1])
    except:
        #pass
        messagebox.showinfo('!!Error', 'Error read file csv กรุณาบันทึกข้อมูลก่อน')

    def prev():
        global countindex
        if countindex == 0:
            countindex = countindex
        else:
            countindex =  countindex - 1
        v_text_title.set(knowledgelist[countindex][0])
        v_text_detail.set(knowledgelist[countindex][1])

    def next():
        global countindex
        if countindex == len(knowledgelist)-1:
            countindex = countindex
        else:
            countindex =  countindex  + 1
        v_text_title.set(knowledgelist[countindex][0])
        v_text_detail.set(knowledgelist[countindex][1])

    
    button_prev = ttk.Button(GUI2, text = '<', command=prev)
    button_prev.place(x=170, y=350)
    button_next = ttk.Button(GUI2, text = '>', command=next)
    button_next.place(x=250, y=350)

    GUI2.mainloop()



flashbutton = os.path.join(path, 'flashcard.png')
flashB = PhotoImage(file=flashbutton)

BFlashcard = ttk.Button(GUI, image = flashB, command=showScrFlashcard)
BFlashcard.place(x=600, y=20)


GUI.mainloop()

