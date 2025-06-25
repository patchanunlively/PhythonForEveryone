
print('----------call เฉยๆ------------')
def hello(friend):
    print('Hi, {}'.format(friend))

hello('John')  #call เฉยๆ
hello('Robert')

print('\n')
print('----------call + return value------------')
def land(width, long):
    cal = width * long
    cal_wa = cal/4
    print(' ที่ดินผืนนี้กว้าง {} ม. ,ยาว {} ม. '.format(width,long))
    print('ที่ดินมีพท. {} ตร.ม.'.format(cal))
    print('ที่ดินมีพท. {} ตร.วา'.format(cal_wa))
    return cal_wa



result_for_used = land(5,15) #call แบบต้องการเอาค่าไปใช้ต้องเอา ตัวแปรรับค่า return
print(result_for_used)


print('\n')
print('---------มี defalut value parameter-------------')

def land(width = 200, long= 480) : #default value
    cal = width * long
    cal_wa = cal/4
    print(' ที่ดินผืนนี้กว้าง {} ม. ,ยาว {} ม. '.format(width,long))
    print('ที่ดินมีพท. {} ตร.ม.'.format(cal))
    print('ที่ดินมีพท. {} ตร.วา'.format(cal_wa))
    return cal_wa



result_for_used = land()
print(result_for_used)
print('{:,.2f}'.format(result_for_used)) #format  มีลูกน้ำ และทศนิยมสองตำแหน่ง

print('\n')
print('----------------------')