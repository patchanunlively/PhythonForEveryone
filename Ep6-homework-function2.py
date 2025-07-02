def find_positon(source_list , find_value = 'ไม่มีใน list'):
    """find position of list"""

    i = 0
    is_find = True

    while is_find and i < len(source_list) :
        if source_list[i] == find_value:
           is_find = False 
        else :
            i = i + 1

    return i

my_list = ['อ่านหนังสือธรรมะใครๆก็ทำได้', 'กินยา', 'ทำวิทยานิพนธ์']
print('--------------------------------')
print(f'my_list : {my_list}')

v_find = 'ทำวิทยานิพนธ์'
result_postion = find_positon(my_list[:], v_find)
if result_postion < 3: #แปลว่าหาเจอ
    print(f'result_postion of {v_find} : {result_postion}')
else:
     print(f'result_postion of {v_find} : Not Found')


v_find = None
result_postion = find_positon(my_list[:]) #none second parameter > used default
if result_postion < 3: #แปลว่าหาเจอ
    print(f'result_postion of {v_find} : {result_postion}')
else:
     print(f'result_postion of {v_find} : Not Found')

