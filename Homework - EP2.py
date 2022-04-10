import turtle
tao = turtle.Pen()
tao.shape('turtle')
def Rectangle():
    tao.goto(0,0)
    for i in range (8):
        tao.forward(80)
        tao.left(45)
    tao.penup()
    tao.goto(10,10)
    tao.pendown()
    for i in range (8):
        tao.forward(80)
        tao.left(45)
    tao.goto(20,20)
    tao.pendown()
    for i in range (8):
        tao.forward(80)
        tao.left(45)
    tao.goto(30,30)
    tao.pendown()
    for i in range (8):
        tao.forward(80)
        tao.left(45)

        
def Rectangle1():
    tao.goto(-10,-10)
    for i in range (8):
        tao.forward(80)
        tao.left(45)
    tao.penup()
    tao.goto(-20,-20)
    tao.pendown()
    for i in range (8):
        tao.forward(80)
        tao.left(45)
    tao.goto(-30,-30)
    tao.pendown()
    for i in range (8):
        tao.forward(80)
        tao.left(45)
    tao.goto(-40,-40)
    tao.pendown()
    for i in range (8):
        tao.forward(80)
        tao.left(45)

def Rectangle2():
    tao.goto(-10,-50)
    for i in range (8):
        tao.forward(80)
        tao.left(45)
    tao.penup()
    tao.goto(-20,-60)
    tao.pendown()
    for i in range (8):
        tao.forward(80)
        tao.left(45)
    tao.goto(-30,-70)
    tao.pendown()
    for i in range (8):
        tao.forward(80)
        tao.left(45)
    tao.goto(-40,-80)
    tao.pendown()
    for i in range (8):
        tao.forward(80)
        tao.left(45)

Rectangle()
Rectangle1()
Rectangle2()

