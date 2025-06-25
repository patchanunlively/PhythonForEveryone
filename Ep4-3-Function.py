print('-----------Define function for reuse----------------')
def functionA():   #Define function for reuse
    print('Hello kitti')
    print('........')
    print('ZZZZ....z...z..................')
    print('Hello Are you hear me?')

functionA()  #call function


print('-----------Define function for reuse-need parameter----------------')
#repeatAgain = parameter of function
#functionB(2) ==> 2 คือ argument ที่ส่งเข้าไป

def functionB(repeatAgain):   #Define function for reuse-Need parameter
    for i in range(repeatAgain):
        print('Hello kitti')
        print('........')
        print('ZZZZ....z...z....')
        print('Hello Are you hear me.........?')

functionB(2)   #call function


