class residence:
    def __init__(self, type_name, address):
        self.type_name = type_name
        self.address = address

    # Method
    def show_residence_description(self):
        print(f'type_name = {self.type_name}')
        print(f'address = {self.address}')


#สืบทอด or inherit class เดิมมา
class person(residence):
    
    def __init__(self,fullname, age, type_name, address):
        super().__init__(type_name, address)
        self.fullname = fullname
        self.age = age


    # Method 
    def get_profile(self):
        print(f'Full Name = {self.fullname}')
        print(f'Age = {self.age}')
        print(f'residence type = {self.type_name}')
        print(f'address = {self.address}')
        


#สร้าง instance or object 
print('\n')
john = person('John' , 20, 'คฤหาสถ์' , 'ลอนดอน tower 88/888 ... ')
john.get_profile()


# print('\n')
# res1 = residence('บ้านเดี่ยว' , '322/1 หมู่2 .....')
# res1.show_residence_description()

# res2 = residence('คอนโด' , '3/8 ถ.xxx .....')
# res2.show_residence_description()