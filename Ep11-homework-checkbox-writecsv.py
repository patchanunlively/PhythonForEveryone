#---write file-----------------------
import csv 
def writecsv(data):
    with open('Ep11-homework-checkbox.csv','a', newline='', encoding='utf-8') as file: 
        fw = csv.writer(file)   
        fw.writerow(data)   #writerow = write 1 row, writerows= write N row

#---GUI-----------------------
from tkinter import *
from tkinter import ttk

def save():
    print('----------------------')
    ck1 = v_checkbox1.get()
    ck_text1 = checkbox1.cget("text")
    print(f'ck1 = {ck1}')
    print(f'Label on checkbox1 = {ck_text1}')

    ck2 = v_checkbox2.get()
    ck_text2 = checkbox2.cget("text")
    print(f'ck2 = {ck2}')
    print(f'Label on checkbox2 = {ck_text2}')

    ck3 = v_checkbox3.get()
    ck_text3 = checkbox3.cget("text")
    print(f'ck = {ck3}')
    print(f'Label on checkbox3 = {ck_text3}')

    data = [ck1, ck_text1, ck2, ck_text2, ck3, ck_text3]
    writecsv(data)  # call write file

    #clear data
    v_checkbox1.set(0)
    v_checkbox2.set(0)
    v_checkbox3.set(0)


GUI = Tk() #คนอื่นอาจจะเรียกว่า root เราเรียก GUI
GUI.title('โปรแกรม To Do list')
GUI.geometry('500x500')

v_checkbox1 = IntVar() 
v_checkbox2 = IntVar() 
v_checkbox3 = IntVar() 

L1 = ttk.Label(GUI, anchor="w", text='\nTo Do List\n', font=('Angsana New',20 ,"bold" ), width = 50)
L1.pack()

checkbox1 = Checkbutton(GUI, anchor="w", text = "ทำการบ้าน", 
                    variable = v_checkbox1, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 30) 

checkbox2 = Checkbutton(GUI, anchor="w",text = "เรียนแคลคูลัส", 
                    variable = v_checkbox2, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 30) 

checkbox3 = Checkbutton(GUI, anchor="w", text = "ถูบ้าน", 
                    variable = v_checkbox3, 
                    onvalue = 1, 
                    offvalue = 0, 
                    height = 2, 
                    width = 30) 

checkbox1.pack() 
checkbox2.pack() 
checkbox3.pack() 

B1 = ttk.Button(GUI, text = 'บันทึก', command = save) #ผุกปุ่มหรือcommand กับ function-save 
B1.pack(pady=10, ipadx=20, ipady=10)

GUI.mainloop()



