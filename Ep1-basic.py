#python is case sensitive
#create this file by program idle  from python (location : Macintosh HD⁩ ▸ ⁨Applications⁩ ▸ ⁨Python 3.13⁩)
#run by menu run>run module > some order not show same real shell

'''
multiple comment
'''
print('------------------------')
#python is case sensitive
#pydroid 3 ใช้เขียน program สำหรับ andriod


print('------------------------')
'''
-install เฉพาะ package ของ version นั้นๆ ex นี้คือ เฉพาะ package numpy
    c:\python312\python.exe -m pip install --upgrade numpy  

-install เช่น
    pip install numpy==0.5.1
    pip install matplotlib==1.3.4    

-เช็ค version python ใน command prompt ไม่แน่ใจว่าต้องใน floder ที่มี project หรือว่าตรงไหนก็ได้ ซึ่งเราสั่ง downgrade vesion ได้ หรืออาจทำเป็น enviroment virtual enviroment
    pip list
'''
print('------------------------')


print('H')
print('B')
print('X')
a='1'
type(a)
b='c'
x=a+b
type(a)
type(b)
type(x)
print(x)
print(a.zfill(3)) #format pad 0 auto to 3 digit 
print(b.upper())
print('parameter a = {}, parameter b = {} , parameter x = {}'.format(a,b,x) )
print(f'parameter a = {a}, parameter b = {b} , parameter x = {x}')
print('\n')
print('------------------------')
print('---------------------------')
print('list(range(0))>>>')
print(list(range(0))) #จริงๆไม่ต้องใส่ print ตอนรันจริงก็ออกค่า แต่ใส่ถ้าจะรันจาก file ไ่ม่ใช่บน shell

print('list(range(1))>>>')
print(list(range(1)))

print('list(range(2))>>>')
print(list(range(2)))



print('---------------------------')
print('list(range(0,3))>>>')
print(list(range(0,3))) #จริงๆไม่ต้องใส่ print ตอนรันจริงก็ออกค่า
print('เจอ 3 ไม่ทำละ')

print('list(range(1,3))>>>')
print(list(range(1,3)))

print('list(range(2,3))>>>')
print(list(range(2,3)))


print('------------ord, char---------------')
print('ord(\'ก\') ข...')
print('char(ord(\'ฃ\'))) #or chr(3587)')
a = ord('ก')
b = ord('ข')
c = ord('ฃ')
xxx = chr(ord('ฃ')) #or chr(3587)
print(a)
print(b)
print(c)
print(xxx)



print('\n')
print('-------------------------')

isTrue = True #boolean 
if isTrue == True : 
    print('True ja')
print(type(isTrue))

isTrue = False #boolean 
if isTrue == False : 
    print('False ja')
print(type(isTrue))

