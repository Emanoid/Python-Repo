import turtle
import os
import random
import math

os.chdir(r"C:\Users\olatunem\OneDrive - Seton Hall University\Extraneous\PYTHON WORKSPACE")

tree_state1 = 'not active'
tree_state2 = 'not active'
tree_state3 = 'not active'
jump_state = 'down'
shift = 0
def main():
    global tree_state1, tree_state2, tree_state3, jump_state, shift

    #Make Screen
    wn = turtle.Screen()
    wn.bgcolor('white')
    wn.title('Skateboard Run')
    wn.screensize(500,500)

    #Make Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color('black')
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pensize(3)
    border_pen.pendown()
    for i in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    #Make Skateboarder
    wn.addshape('Dinn.gif')
    din = turtle.Turtle()
    din.shape('Dinn.gif')
    din.penup()
    din.speed(0)
    din.setposition(-210,-230)

    #Game Over Message
    wn.addshape('gameover.gif')
    gam = turtle.Turtle()
    gam.shape('gameover.gif')
    gam.penup()
    gam.speed(0)
    gam_shift = 20
    gam.setposition(-300,0)
    gam.hideturtle()

    #Make Tree
    wn.addshape('tr (1).gif')
    wn.addshape('tr (2).gif')
    wn.addshape('tr (3).gif')
    tree_shift = 15

    tree1 = turtle.Turtle()
    tree1.shape('tr (1).gif')
    tree1.penup()
    tree1.speed(0)
    tree1.setposition(400,-200)
    tree1.hideturtle()

    tree2 = turtle.Turtle()
    tree2.shape('tr (2).gif')
    tree2.penup()
    tree2.speed(0)
    tree2.setposition(400,-250)
    tree2.hideturtle()

    tree3 = turtle.Turtle()
    tree3.shape('tr (3).gif')
    tree3.penup()
    tree3.speed(0)
    tree3.setposition(400,-230)
    tree3.hideturtle()

    #Compute Collision
    def collision(a,b):
        x1 = a.xcor()
        x2 = b.xcor()
        y1 = a.ycor()
        y2 = b.ycor()
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return dist <= 70

    def jump():
        global jump_state, shift
        if din.ycor() == -230:
            jump_state = 'up'
            shift = 20

   

    #Keyboard Commands
    turtle.listen()
    turtle.onkey(jump, 'Up')

    h = 1
    while True:
        #Execute Simulation
        #Game Over Message
        x = gam.xcor()
        x += gam_shift
        if x >= 290:
            gam_shift *= -1
        if x <= -290:
            gam_shift *= -1
        gam.setx(x)
        #Tree Display
        if tree1.xcor() <= 300:
            tree1.showturtle()
        if tree2.xcor() <= 300:
            tree2.showturtle()
        if tree3.xcor() <= 300:
            tree3.showturtle()
        if tree1.xcor() <= -300:
            tree1.hideturtle()
            tree1.setposition(400,-200)
            tree_state1 = 'not active'
        if tree2.xcor() <= -300:
            tree2.hideturtle()
            tree2.setposition(400,-250)
            tree_state2 = 'not active'
        if tree3.xcor() <= -300:
            tree3.hideturtle()
            tree3.setposition(400,-230)
            tree_state3 = 'not active'
        #Tree Assign
        if tree_state1 == 'not active' and tree_state2 == 'not active' and tree_state3 == 'not active':
            h = random.randint(1,3)
        #Tree Big Bang
        if h == 1 and tree_state2 == 'not active' and tree_state3 == 'not active':
            tree_state1 = 'active'
            x = tree1.xcor()
            x -= tree_shift
            tree1.setx(x)            
        if h == 2 and tree_state1 == 'not active' and tree_state3 == 'not active':
            tree_state2 = 'active'
            x = tree2.xcor()
            x -= tree_shift
            tree2.setx(x)
        if h == 3 and tree_state1 == 'not active' and tree_state2 == 'not active':
            tree_state3 = 'active'
            x = tree3.xcor()
            x -= tree_shift
            tree3.setx(x)
        #Jump Mechanics
        if jump_state == 'up':
            y = din.ycor() + shift
            din.sety(y)
            if y == 50:
                jump_state = 'down'
        if jump_state == 'down' and din.ycor() > -230:
            y = din.ycor() - shift
            din.sety(y)
        #Collision Handler
        if collision(din,tree1) or collision(din,tree2) or collision(din,tree3):
            gam.showturtle()
            tree_shift = 0

main()
