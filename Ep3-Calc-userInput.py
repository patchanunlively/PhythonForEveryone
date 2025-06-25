
a=3+2
b=10/3
c=3//2   #=1 คือ ค่าที่หารได้
d=10%3   #=1  mod หารหาเศษ

print('a=3+2')
print('b=10/3')
print('c=3//2   #=1 คือ ค่าที่หารได้')
print('d=10%3   #=1  mod หารหาเศษ')

print('\n')

print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
print(f'd={d}')

print('\n')
print('-----------------------')

tiles = 10 #มีกระเบื้อง 
pieces = 3 #1แถวต้องใช้กี่แผ่น
#ถ้าต้องการใช้กระเบื้องเศษที่เหลือ ปูให้หมดอีกแถวต้องซื้อเพิ่มเท่าไหร่?

total_row = tiles//pieces  
remain_tiles = tiles%pieces
buy_more = pieces - remain_tiles


print(f'มีกระเบื้อง = {tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้ = {pieces} แผ่น')
print('---calc---')
print('ถ้าไม่ซื้อเพิ่มจะสามารถปูกระเบื้องได้ {} แถว' .format(total_row))
print('เหลือ {} แผ่น' .format(remain_tiles))
print('ควรซื้อเพิ่ม {} แผ่น' .format(buy_more))


print('\n')
print('---------INPUT EX.--------------')

tiles = int(input('#มีกระเบื้อง ?')) #change to input and cast str-->int
pieces = int(input('#1แถวต้องใช้กี่แผ่น?'))  #change to input and cast str-->int
#ถ้าต้องการใช้กระเบื้องเศษที่เหลือ ปูให้หมดอีกแถวต้องซื้อเพิ่มเท่าไหร่?

total_row = tiles//pieces   
remain_tiles = tiles%pieces
buy_more = pieces - remain_tiles


print(f'มีกระเบื้อง = {tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้ = {pieces} แผ่น')
print('---calc---')
print('ต้องปูกระเบื้องทั้งหมด {} แถว' .format(total_row))
print('เหลือ {} แผ่น' .format(remain_tiles))
print('ควรซื้อเพิ่ม {} แผ่น' .format(buy_more))


print('\n')
print('---------Try Except EX.--------------')

try: #add line
    tiles = int(input('#มีกระเบื้อง ?'))
    pieces = int(input('#1แถวต้องใช้กี่แผ่น?')) 
    #ถ้าต้องการใช้กระเบื้องเศษที่เหลือ ปูให้หมดอีกแถวต้องซื้อเพิ่มเท่าไหร่?
except: #add line
    print('Please key number , not string') #add line
    tiles = int(input('#มีกระเบื้อง ?'))
    pieces = int(input('#1แถวต้องใช้กี่แผ่น?'))
    

total_row = tiles//pieces   
remain_tiles = tiles%pieces
buy_more = pieces - remain_tiles


print(f'มีกระเบื้อง = {tiles} แผ่น')
print(f'1 แถวปูกระเบื้องได้ = {pieces} แผ่น')
print('---calc---')
print('ต้องปูกระเบื้องทั้งหมด {} แถว' .format(total_row))
print('เหลือ {} แผ่น' .format(remain_tiles))
print('ควรซื้อเพิ่ม {} แผ่น' .format(buy_more))



print('\n')
print('---------DICTIONARY--------------')

dictionary_money ={'Mother':1000, 'Father':20}


father_want_money = int(input('#พ่ออยากยืมแม่ไปซื้อขนมปังปิ้งเป็นเงิน ?'))
mother_give_per_day =  int(input('#แม่ผ่อนให้ยืม้วันละ'))
#พ่อต้องรอกี่วันถึงได้กินขนมปังปิ้ง?
#แม่จะเหลือกี่บาท

    
father_borrow = father_want_money - dictionary_money['Father']

if father_borrow % mother_give_per_day == 0:
    father_recieve_all_how_many_day = father_borrow // mother_give_per_day
else :
    father_recieve_all_how_many_day = (father_borrow // mother_give_per_day)+1


mother_remain = dictionary_money['Mother']-father_borrow

print('\n')
print('แต่ละคนมีเงิน >>')
print( dictionary_money)
print('\n')

print(f'#พ่ออยากยืมแม่ไปซื้อขนมปังปิ้งเป็นเงิน = {father_want_money} บาท')
print(f'#แม่ผ่อนให้ยืม้วันละ = {mother_give_per_day} บาท')
print('---calc---')
print('แปลว่าพ่อขอยืมเพิ่มอีก {} บาท' .format(father_borrow))
print('พ่อต้องรออีก {} ก็จะได้กินขนมปังปิ้ง' .format(father_recieve_all_how_many_day))
print('แม่จะเหลือ {} บาท' .format(mother_remain))




