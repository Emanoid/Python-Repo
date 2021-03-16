'''
Towers of Hanoi: In the classic problem of the Towers of Hanoi, 
you have 3 towers and N disks of different sizes which can slide
 onto any tower. The puzzle starts with disks sorted in ascending
  order of size from top to bottom (Le., each disk sits on top
   of an even larger one). You have the following constraints: 
(1) Only one disk can be moved at a time. 
(2) A disk is slid off the top of one tower onto another tower. 
(3) A disk cannot be placed on top of a smaller disk. 
Write a program to move the disks from the first tower to the last using stacks. '''


import Stacks
import turtle
import os

os.chdir(r"C:\Users\olatunem\OneDrive - Seton Hall University\Extraneous\PYTHON WORKSPACE")

N = int(input('Enter Number of Disks: '))
Tower1 = Stacks.Stack_Dynamic_Array()
Tower2 = Stacks.Stack_Dynamic_Array()
Tower3 = Stacks.Stack_Dynamic_Array()

class Disk:
    def __init__(self,size):
        self.size = size

    def getsize(self):
        return self.size

    def move(self,stacka,stackb):
        if stacka.isEmpty() == False:
            if stackb.isEmpty() == True:
                stackb.push(stacka.pop())
            else:
                if stackb.top().getsize() > self.getsize():
                    stackb.push(self)
                    stacka.pop()
                else:
                    print('Cannot place a larger disk on a small disk')
        else:
            print('Initial Stack is Empty')

def stackpour(n,stack):
    if n > 0:
        stack.push(Disk(n))
        stackpour(n-1,stack)

def diskmove(stacka,stackb):
    stacka.top().move(stacka,stackb)                

def draw():
    os.chdir(r"C:\Users\olatunem\OneDrive - Seton Hall University\Extraneous\PYTHON WORKSPACE")
    #Make Screen
    wn = turtle.Screen()
    wn.bgcolor('white')
    wn.title('Skateboard Run')

    #Make Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color('black')
    border_pen.penup()
    border_pen.setposition(-500,-500)
    border_pen.pensize(3)
    border_pen.pendown()
    for i in range(4):
        border_pen.fd(1000)
        border_pen.lt(90)
    border_pen.hideturtle()

    #Make Towers
    T1 = turtle.Turtle()
    T1.pensize(5)
    T1.penup()
    T1.speed(0)
    T1.setposition(-385,-290)
    for i in range(3):
        T1.pendown()
        T1.fd(175)
        T1.penup()
        x = T1.xcor() + 100
        T1.setposition(x,-290)
    T1.penup()
    T1.setposition(-400+15+88,-290)
    for i in range(3):
        T1.pendown()
        T1.lt(90)
        T1.forward(500)
        T1.rt(90)
        T1.penup()
        T1.setposition(T1.xcor()+280,-290)

    #Skeleton Disks
    wn.addshape('one.gif')
    wn.addshape('two.gif')
    wn.addshape('three.gif')
    wn.addshape('four.gif')
    wn.addshape('five.gif')
    wn.addshape('six.gif')
    wn.addshape('seven.gif')
    wn.addshape('eight.gif')
    wn.addshape('nine.gif')
    wn.addshape('ten.gif')
    #Skeleton BASE & SHAFT
    wn.addshape('base.gif')
    wn.addshape('shaft.gif')
    #Menu Guide
    wn.addshape('guide.gif')
    wn.addshape('T1.gif')
    wn.addshape('T2.gif')
    wn.addshape('T3.gif')
    wn.addshape('win.gif')

    #Make Menu
    G = turtle.Turtle()
    G.penup()
    G.setposition(0,250)
    G.shape('guide.gif')
    t1 = turtle.Turtle()
    t1.shape('T1.gif')
    t2 = turtle.Turtle()
    t2.shape('T2.gif')
    t3 = turtle.Turtle()
    t3.shape('T3.gif')
    t1.penup()
    t2.penup()
    t3.penup()
    win = turtle.Turtle()
    win.penup()
    t1.speed(0)
    t2.speed(0)
    t3.speed(0)
    win.hideturtle()
    win.shape('win.gif')
    win.setposition(-450,0)
    winshift = 10    
    t1.setposition(-297,-310)
    t2.setposition(-17,-310)
    t3.setposition(263,-310)
    
    #Make Disks
    ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN = turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle()
    ONE.shape('one.gif')
    TWO.shape('two.gif')
    THREE.shape('three.gif')
    FOUR.shape('four.gif')
    FIVE.shape('five.gif')
    SIX.shape('six.gif')
    SEVEN.shape('seven.gif')
    EIGHT.shape('eight.gif')
    NINE.shape('nine.gif')
    TEN.shape('ten.gif')
    ONE.penup()
    TWO.penup()
    THREE.penup()
    FOUR.penup()
    FIVE.penup()
    SIX.penup()
    SEVEN.penup()
    EIGHT.penup()
    NINE.penup()
    TEN.penup()
    ONE.hideturtle()
    TWO.hideturtle()
    THREE.hideturtle()
    FOUR.hideturtle()
    FIVE.hideturtle()
    SIX.hideturtle()
    SEVEN.hideturtle()
    EIGHT.hideturtle()
    NINE.hideturtle()
    TEN.hideturtle()
    DISKS = [None,ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN]
    for i in range(1,11):
        DISKS[i].speed(0)
    
    #Tower Dimensions
    Towerx = ['None',-297,-17,263]
    Towery = ['None',-270,-220,-170,-120,-70,-20,30,80,130,180]

    def T12T2():
        diskmove(Tower1,Tower2)
    def T12T3():
        diskmove(Tower1,Tower3)
    def T22T1():
        diskmove(Tower2,Tower1)
    def T22T3():
        diskmove(Tower2,Tower3)
    def T32T1():
        diskmove(Tower3,Tower1)
    def T32T2():
        diskmove(Tower3,Tower2)

    #Keyboard Commands
    turtle.listen()
    turtle.onkey(T12T2, 1)
    turtle.onkey(T12T3, 2)
    turtle.onkey(T22T1, 3)
    turtle.onkey(T22T3, 4)
    turtle.onkey(T32T1, 5)
    turtle.onkey(T32T2, 6)

    while True:
        #Win  Message
        x = win.xcor()
        x += winshift
        if x >= 445:
            winshift *= -1
        if x <= -445:
            winshift *= -1
        win.setx(x)
        #Tracks position of Disks
        Twr1 = Tower1.iter()
        Twr2 = Tower2.iter()
        Twr3 = Tower3.iter()
        for i in Twr1:
            DISKS[i].setposition(Towerx[1],Towery[Twr1.index(i)+1])
            DISKS[i].showturtle()
        for i in Twr2:
            DISKS[i].setposition(Towerx[2],Towery[Twr2.index(i)+1])
            DISKS[i].showturtle()
        for i in Twr3:
            DISKS[i].setposition(Towerx[3],Towery[Twr3.index(i)+1])
            DISKS[i].showturtle()
        if Tower1.isEmpty() == True and Tower2.isEmpty() == True:
            win.showturtle()

stackpour(N,Tower1)
draw()
