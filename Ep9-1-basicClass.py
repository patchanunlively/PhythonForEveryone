class Theater:
    # Attribute
    theaterName = 'Uncle Engineer Theater'
    title = 'แฟนฉัน'
    price = 80

    # Method
    def hello(self):
        print('Hi everyone - from class class Theater')


#สร้าง instant or object 
print('\n')
movie01 = Theater()
print(movie01.theaterName)
print(movie01.title)
print(movie01.price)
movie01.hello()

#------------------------------

#แบบไม่อยาก fixed ค่าต่างๆ
class TheaterFlexible:
    # Attribute
    theaterName = 'Uncle Engineer Theater'
    #title = 'แฟนฉัน'
    #price = 80

    # Constructor = คือเมธอดพิเศษ (special method) ที่ถูกเรียกใช้งานโดยอัตโนมัติเมื่อมีการสร้างอินสแตนซ์ (instance) หรือวัตถุ (object) >>> __init_(self, <attributes….>) ห้าม return ค่า
    def __init__(self, title, price):
        self.title = title
        self.price = price

    # Method
    def hello(self):
        print('Hi everyone - from class TheaterFlexible')


#สร้าง instance or object 
print('\n')
movie02 = TheaterFlexible('อาม่า' , 150)
print(movie02.theaterName)
print(movie02.title)
print(movie02.price)
movie02.hello()


#สร้าง instance or object 
print('\n')
movie03 = TheaterFlexible('Matrix' , 120)
print(movie03.theaterName)
print(movie03.title)
print(movie03.price)
movie03.hello()


#----------------------------

#สืบทอด or inherit class เดิมมา
class Customer(TheaterFlexible):
    
    # Constructor = คือเมธอดพิเศษ (special method) ที่ถูกเรียกใช้งานโดยอัตโนมัติเมื่อมีการสร้างอินสแตนซ์ (instance) หรือวัตถุ (object) >>> __init_(self, <attributes….>) ห้าม return ค่า
    def __init__(self,fullname, age, title, price, seats):
        super().__init__(title, price)
        self.fullname = fullname
        self.age = age
        self.seats = seats
        self.money = 1000

    # Method 
    def buyTicket(self):
        #cal price
        self.total = self.price * self.seats

        self.money -= self.total

        print(f'Customer Name = {self.fullname}')
        print(f'Age = {self.age}')
        print(f'Story = {self.title}')
        print(f'seats = {self.seats}')
        print(f'Remain = {self.money}')



    def hello(self):
        print('Hi everyone - from class Customer')


#สร้าง instance or object 
print('\n')
movie04 = Customer('petch' , 20, 'ขบวนการหวานใจ' , 120, 2)
movie04.buyTicket()
movie04.hello()


   