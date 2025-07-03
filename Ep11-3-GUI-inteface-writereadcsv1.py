#---write file-----------------------
import csv 
def writecsv(data):
    with open('knowlendge2.csv','a', newline='', encoding='utf-8') as file: 
        fw = csv.writer(file)   
        fw.writerow(data)   #writerow = write 1 row, writerows= write N row




#---GUI-----------------------

from tkinter import * #import all function inside main package
from tkinter import ttk #<<< เปลี่ยน import แล้วเรียกข้างล่าง



GUI = Tk() #คนอื่นอาจจะเรียกว่า root เราเรียก GUI
GUI.title('โปรแกรมบันทึกความรู้ By Loong-แบบสวยขึ้น')
GUI.geometry('500x500')



L1 = ttk.Label(GUI, text='Title', font=('Angsana New',18))
L1.pack()

v_tit = StringVar()  
E1 = ttk.Entry(GUI, textvariable = v_tit, font=('Angsana New',20),width=50)   #เอาค่าจาก E1 ไปเก็บในตัวแปร v_tit
E1.pack()




L3 = ttk.Label(GUI, text='Description', font=('Angsana New',18))
L3.pack()

T1 = Text(GUI, font=('Angsana New',18), height = 8, width=56) 
T1.pack()





def save():
    tit = v_tit.get()
    textbox = T1.get(1.0,"end-1c")   # >>  "end-1c" คือ ดึงมาแบบเอา \n ตัวสุดท้ายออกให้
    #textbox = T1.get(1.0,END)  >>  "END" เฉยๆ คือดึง default ซึ่งใส่ \n ตอนท้ายให้ด้วย
    print('----------------------')
    print(tit)
    print([textbox])    #print(textbox) 
    print('----------------------') 
    data = [tit, textbox]
    writecsv(data)  # call write file

    #clear data
    v_tit.set('')
    T1.delete('1.0', END) 


B1 = ttk.Button(GUI, text = 'บันทึก', command = save) #ผุกปุ่มหรือcommand กับ function-save 
B1.pack(pady=10, ipadx=20, ipady=10)

GUI.mainloop()



