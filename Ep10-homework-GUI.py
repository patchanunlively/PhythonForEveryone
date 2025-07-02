from tkinter import *
from tkinter import ttk

GUI = Tk() 
GUI.title('โปรแกรมบันทึกรายจ่าย')
GUI.geometry('500x500')



L1 = ttk.Label(GUI, text='รายจ่าย', font=('Angsana New',18))
L1.pack()
T1 = Text(GUI, font=('Angsana New',18), height = 8, width=56) 
T1.pack()

L2 = ttk.Label(GUI, text='ราคาต่อหน่วย', font=('Angsana New',18))
L2.pack()
E1 = ttk.Entry(GUI, font=('Angsana New',20),width=50) 
E1.pack()

L3 = ttk.Label(GUI, text='จำนวน (หน่วย)', font=('Angsana New',18))
L3.pack()
E2 = ttk.Entry(GUI, font=('Angsana New',20),width=50) 
E2.pack()

B1 = ttk.Button(GUI, text = 'บันทึก')
B1.pack(pady=10, ipadx=20, ipady=10)

GUI.mainloop()
