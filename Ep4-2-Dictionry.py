numberDictionary = {'31001':'John', '31002':'Smith', '31003':'Jonathan'} #{'key':'value'}
print(numberDictionary['31001'])


print('\n---for--print value')
for i in numberDictionary:
    print(i)


print('\n---for--print keys and value')
for i in numberDictionary.items():
    print(i)



print('\n---for--print keys and value แบบระบุตำแหน่ง')
for i in numberDictionary.items():
    print(i[0] + ' ' + i[1])




print('\n---for--print keys')
for i in numberDictionary.keys():
    print(i)


print('\n---for--print values')
for i in numberDictionary.values():
    print(i)


a_dict = {'x':'1', 'y':2}
a_dict['z'] = 3 #เพิ่ม key and value ต่อท้ายจากที่มีเดิมสอง key
print(a_dict)
 
    
