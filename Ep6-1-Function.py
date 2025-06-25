
print('--------section 1-------------')
def greet_user():
    """Display a simple greeting.<<< description of function""" #คำอธิบายฟังก์ชั่น กรณีที่เราเรียก help ของ  function greet_user มันจะแสดงให้
    print("Hello!")


def greet_user2():
    print("Hello!2")


greet_user()    
greet_user2()


print('------dir()-----')
dir()  #ตัวนี้ต้องเรียกที่ shell >>>ใช้ดูว่า program นี้มีการเรียกใช้อะไรได้บ้าง  
'''
ex. เมื่อเรียก dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'greet_user', 'greet_user2']
'''

print('-----call help-----')
help(greet_user) #ใช้ดูว่า function นี้ มี help เป็นอะไรหรือมีคำอธิบายอะไร
help(greet_user2) 
help(print)
