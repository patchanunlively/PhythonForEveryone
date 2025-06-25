#list สามารถเก็บได้หลาย data type in list
my_list = ['string', 1,1.0, {'2001':'นาย A', '2002':'นาย B'}, [2,'x']]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])



carsList = ['toyota', 'honda', 'benz']
print(carsList)


print('\n')
carsList.append('byd')
print('carsList.append(\'byd\')')
print(carsList)


print('\n')
carsList.remove('honda')
print('carsList.remove(\'honda\')')
print(carsList)


print('\n')
print('print(carsList[0])')
print(carsList[0])





print('\n')
print('for c in carsList: print(c)')
for c in carsList:
        print(c)


print('\n')
print('print(*carsList)')
print(*carsList)



print('\n')
print('for i,c in enumerate(carsList):print(i,c)')
for i,c in enumerate(carsList):
    print(i,c)


print('\n')
print('for i,c in enumerate(carsList, start=0):print(i,c)')
for i,c in enumerate(carsList, start=0): #add start=0
    print(i,c)


print('\n')
print('for i,c in enumerate(carsList, start=1):print(i,c)')
for i,c in enumerate(carsList, start=1): #add start=1
    print(i,c)



print('\n----replace----')
print('replace to element 0 ==> carsList[0] = \'NEW-REPLACE\' ==> print(carsList)')
print('Before replace element 0')
print(carsList)
carsList[0] = 'NEW-REPLACE'
print('after replace...')
print(carsList)



print('\n----POP ดึง Last ออกมาเลย เลยจะหายไป ----')
print(carsList)
last_carsList = carsList.pop()
print(last_carsList)
print(carsList)

print('\n----POP ดึง first ออกมาเลย เลยจะหายไป ----')
print(carsList)
first_carsList = carsList.pop(0)
print(first_carsList)
print(carsList)


print('\n----len----')
print(len(carsList))


print('\n----Delete from last element position ----')
carsList2 = ['x', 'a', 'y', 'z','x4', 'x2', 'x1']
print(carsList2)
print('del carsList2(-1)')
del carsList2[-1]
print(carsList2)

print('\n----Delete from last element position ----')
carsList3 = ['x', 'a', 'y', 'z','x4', 'x2', 'x1']
print(carsList3)
print('del carsList3(-2)')
del carsList3[-2]
print(carsList3)


print('\n----SORT----')
sortList = ['x', 'a', 'y', 'z','x4', 'x2', 'x1']
print(sortList)
print('sortList.sort()')
sortList.sort()
print(sortList)
