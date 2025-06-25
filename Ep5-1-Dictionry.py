#dictionary มักใช้กับการเก็บข้อมูลเพื่อหา unique เช่น เบอร์โทรนั้นคือ ใคร..., บัตรประชาชนนี้ เป็นใคร
#dictionary มี key, value
import turtle

def rect(tao_pen_p, tao_dictionary_p):
    tao_pen_p.color(tao_dictionary_p['color'])
    for i in range(4):
        tao_pen_p.forward(tao_dictionary_p['distance'])
        tao_pen_p.left(90)
        print('in for')
    print('in in def')
print('not in defffff') #NOT in deffffff ja



            
tao_pen_1 = turtle.Pen()
tao_pen_1.shape('turtle')
tao_dictionary_1 = {'color':'green', 'distance':100}
rect(tao_pen_1, tao_dictionary_1)



tao_pen_2 = turtle.Pen()
tao_pen_2.shape('turtle')
tao_dictionary_2 = {'color':'blue', 'distance':50}
rect(tao_pen_2, tao_dictionary_2)


