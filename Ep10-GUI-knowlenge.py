
'''
ปกติใช้แบบนี้ก็ได้ แต่ก็จะต้องพิพม์ทีละตัว  
from tkinter import Button, Tk

ถ้าไม่ใส่ตอนใช้ก็จะต้องเรียกทีละตัว
import tkinter
ฺB = tkinter.Button()


แต่กรณีเรียกมาหมดเลย  จะ import หมดตอนใช้ก็เรียกได้เลย
from tkinter import * #import all function inside main package
ฺB = Botton()

ส่วนนี้ลองเรียก import แล้ว print(dir()) เพื่อดูว่ามันเอาอะไรเพิ่มให้ได้
ซึ่งก็ดูได้ด้วว่า แต่ละ function ใช้ยังไงจาก help(functionName) ex. help(Botton) หรือใส่ print(help(Botton))
'''
#----------------------------------------------
from tkinter import * #import all function inside main package

GUI = Tk() #คนอื่นอาจจะเรียกว่า root เราเรียก GUI
GUI.title('โปรแกรมบันทึกความรู้ By Loong')
GUI.geometry('500x500')
'''
widget Entry คือ textBox
    กำหนดตำแหน่งได้สามแบบ
    grid = บอกเป็นตารางว่าตำแหน่งตรงไหน row column
    pack = ไว้ไหนแล้วก็เรียงจากบนลงล่าง
    place = ใส่ x,y asix > ex. E1.place(x=300, y = 300)

'''
E1 = Entry(GUI, font=('Angsana New',20)) 
E1.pack()


#------------------เปลี่ยนเป็นแบบ interface สวยขึ้น----------------------------
from tkinter import * #import all function inside main package
from tkinter import ttk #<<< เปลี่ยน import แล้วเรียกข้างล่าง

GUI = Tk() #คนอื่นอาจจะเรียกว่า root เราเรียก GUI
GUI.title('โปรแกรมบันทึกความรู้ By Loong-แบบสวยขึ้น')
GUI.geometry('500x500')


L1 = ttk.Label(GUI, text='หัวข้อความรู้', font=('Angsana New',18))
L1.pack()

E1 = ttk.Entry(GUI, font=('Angsana New',20),width=50) 
E1.pack()


L2 = ttk.Label(GUI, text='รายละเอียด', font=('Angsana New',18))
L2.pack()

T1 = Text(GUI, font=('Angsana New',18), height = 8, width=56) 
T1.pack()

B1 = ttk.Button(GUI, text = 'บันทึก')
B1.pack(pady=10, ipadx=20, ipady=10)

GUI.mainloop()


#------------------เปลี่ยนเป็นแบบ interface สวยขึ้นอีก = python tkinter ttkbootstrap ไปลองหาเองทำดู----------------------------


