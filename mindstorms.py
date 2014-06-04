import turtle

window = turtle.Screen()
window.bgcolor("yellow")

brad = turtle.Turtle()
brad.shape("turtle")
brad.color("red")
brad.speed(20)

    
def draw_square(smth):
    for n in range(1,5):
        brad.forward(150)
        brad.right(90)


def square_circle():
    for n in range(1,40):
        draw_square(brad)
        brad.right(10)

        
        
def circle(x, y):
    angie = turtle.Turtle()
    angie.shape("square")
    angie.color("blue")
    angie.speed(x)
    angie.circle(y)
    
def triangle(x, y):
    colin = turtle.Turtle()
    colin.shape("circle")
    colin.color("green")
    colin.speed(x)
    for n in range(1,4):
        colin.left(120)
        colin.forward(y)

def initials():
    me = turtle.Turtle()
    me.shape("turtle")
    me.color("blue")
    me.speed(10)
    me.left(90)
    me.forward(250)
    for n in range(1,4):
        me.right(90)
        me.forward(100)
    me.back(300)
    me.left(90)
    me.forward(200)
    me.color("blue")
    me.right(90)
    me.forward(90)
    
    
        
draw_square(brad)
circle(5, 100)
triangle(5, 150)       
square_circle()
    
initials()

window.exitonclick()


