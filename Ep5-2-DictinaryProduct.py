#dictionary ซ้อน dictionay
product_dict = {
                'pen':{'ราคา':50,  'สี':'เขียว'}, 
                'ยางลบ':{'ราคา':3,  'สี':'ขาว'},
                'pencil':{'ราคา':100,  'สี':'หลายสี'},
               }

r_u_continue = 'Y'
while r_u_continue == 'Y':
    print('---------------------')
    p_key = input('Product Name = ? ')
    print('\n')

    if p_key in product_dict:
        print(f'ANS >>> Product Name : {p_key} \nPrice : {product_dict[p_key]['ราคา']} \nColor : {product_dict[p_key]['สี']}')
    else:
        print('ANS >>> Not Found product')
    print('\n')
    r_u_continue = input('Would you like to input the Product Name again (Y/N)?\n')
    print('\n')

#การออกจาก whil ให้กด ctrl+c , mac command +q ปิด program เลย