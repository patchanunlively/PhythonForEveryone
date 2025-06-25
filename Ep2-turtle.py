#draw squre by turtle

import turtle
tao = turtle.Pen()
type(tao)
tao.shape('turtle')



#draw basic -by read
tao.color('red')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)


#clear draw and set turtle to black
tao.reset()



for i in range(4):
    tao.color('pink')
    tao.forward(100)
    tao.left(90)


print('---------------------------')
print('time to draw 8 เหล่ียม = ')
print(360/45)

for i in range(8):
    print(f'i={i}')
    tao.color('blue')
    tao.forward(100)
    tao.left(45)


print('---------------------------')



    
#clear draw and set turtle to black
tao.reset()

tao.up() #ยกปากกา เลยจะไม่วาด
tao.color('pink')
tao.goto(30,30)
for i in range(4):
    tao.forward(100)
    tao.left(90)


tao.down() #วางปากกา เลยจะวาด
tao.color('yellow')
tao.goto(30,30)
for i in range(4):
    tao.forward(50)
    tao.left(90)


tao.color('pink')
tao.goto(30,30)
for i in range(4):
    tao.forward(100)
    tao.left(90)


tao.color('blue')
tao.goto(30,40)   #asix(x,y)
for i in range(4):
    tao.forward(100)
    tao.left(90)
print('---------------------------')




tao1 = turtle.Pen()
tao2 = turtle.Pen()

taoListJa = [] #สร้าง list
taoListJa.append(tao)
taoListJa.append(tao1)
taoListJa.append(tao2)

print(taoListJa)

taoListJa[0].color('green')
taoListJa[0].forward(200)
taoListJa[0].backward(200)

taoListJa[1].color('blue')
taoListJa[1].goto(90,90)   #asix(x,y)
taoListJa[1].forward(90)
taoListJa[1].backward(90)


taoListJa[2].color('black')
taoListJa[2].goto(-20,-100)   #asix(x,y)
taoListJa[2].forward(50)
taoListJa[2].backward(50)









          
          

    








          
          

    
