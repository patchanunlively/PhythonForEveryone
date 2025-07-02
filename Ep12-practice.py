
#---write file-----------------------
import csv 
def writecsv(data):
    csvfile = os.path.join(path,fileNameCsv)
    with open(csvfile,'a', newline='', encoding='utf-8') as file: 
        fw = csv.writer(file)   
        fw.writerow(data)   #writerow = write 1 row, writerows= write N row



#---GUI-----------------------

from tkinter import * 
from tkinter import ttk 
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



path = os.getcwd() + "/Ep12"
print('Path = ', path)

fileNameCsv = "Ep12.csv"

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

