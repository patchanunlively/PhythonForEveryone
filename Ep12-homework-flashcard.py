#---GUI-----------------------
from tkinter import * 
from tkinter import ttk 
import csv
import os
from PIL import Image, ImageTk  #pip install Pillow <<< run on cmd or terminal(pip3)
import random

def readcsv():
    csvfile = os.path.join(path,fileNameCsv)
    with open(csvfile, newline='', encoding='utf-8') as file:  
        fr = csv.reader(file)
        data = list(fr)
        return data

global current_index #global ใน Python คือตัวแปรที่ถูกประกาศนอกฟังก์ชันใดๆ ทำให้สามารถเข้าถึงและแก้ไขค่าได้จากทุกส่วนของโปรแกรม
current_index = 0

def checkAnswer():
    if v_answer.get() == flash_card_list[current_index][0]: #flash_card_list[current_index][0] = answer of current image
        list_ans_correct = ["!! YESSSS ","Good Job", "Very Good", "Awesome","All right!"]
        response_check = random.choice(list_ans_correct) + " : " + flash_card_list[current_index][0] + " is Correct"
    else:
        ist_ans_wrong = ["Not Correct", "Try again", "That\'s incorrect, but I\'m getting closer."]
        response_check = random.choice(ist_ans_wrong)
    v_response_check.set(response_check)
    

def nextQuestion():
    global current_index

    v_response_check.set('') 
    v_answer.set('')

    if current_index == len(flash_card_list)-1:
        current_index = current_index
    else:
        current_index =  current_index  + 1
    flash_card_img_file_path = os.path.join(path ,"Question-flashCard")
    flash_card_img_file_path = os.path.join(flash_card_img_file_path ,  flash_card_list[current_index][1])  #flash_card_list[0][1] => image name
    #print('flash_card_img_file_path yyy', flash_card_img_file_path)
    img = Image.open(flash_card_img_file_path)
    img = img.resize((100, 100), Image.LANCZOS) # ปรับขนาดรูปภาพให้พอดีกับ Label (optional)
    v_photo = ImageTk.PhotoImage(img)
    image_label.configure(image=v_photo)
    image_label.image = v_photo # การเก็บ reference นี้สำคัญมากเพื่อป้องกัน garbage collection


path = os.getcwd() 
path = os.path.join(path , "Ep12")  
#print('Path = ', path)
fileNameCsv = "Ep12-homework-flashcard-Question.csv"


flash_card_list = readcsv()
#print("flash_card_list",flash_card_list)
flash_card_img_file_path = os.path.join(path ,"Question-flashCard")
flash_card_img_file_path = os.path.join(flash_card_img_file_path , flash_card_list[current_index][1])  #flash_card_list[0][1] => image name
#print('xxxxx', flash_card_img_file_path)
img = Image.open(flash_card_img_file_path)
img = img.resize(( 100, 100), Image.LANCZOS) # ปรับขนาดรูปภาพให้พอดีกับ Label (optional)


GUI = Tk() #คนอื่นอาจจะเรียกว่า root เราเรียก GUI
GUI.title('Flash Card-Game')
GUI.geometry('500x500')

F1 = Frame(GUI)
F1.place(x=10, y=10)


v_photo = ImageTk.PhotoImage(img)
image_label = Label(F1, image = v_photo, width=100, height=100) 
image_label.pack()

B2 = ttk.Button(F1, text = 'Next Question...',command = nextQuestion) 
B2.pack(anchor="e")

L1 = ttk.Label(F1, text='Your Ans : ', font=('Angsana New',18)) 
L1.pack()

v_answer = StringVar()  
E1 = ttk.Entry(F1, textvariable = v_answer, font=('Angsana New',20),width=30)   #เอาค่าจาก E1 ไปเก็บในตัวแปร v_answer
E1.pack()

B1 = ttk.Button(F1, text = 'Check Answer',command = checkAnswer) 
B1.pack()

v_response_check = StringVar()
L0 = ttk.Label(F1, textvariable = v_response_check, font=('Angsana New',18)) #for show response check ans
L0.pack()

GUI.mainloop()

