'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of 
grid with r rows and c columns. The robot can only move in two directions,
 right and down, but certain cells are "off limits" such that the robot 
 cannot step on them. Design an algorithm to find a path for the robot
  from the top left to the bottom right. '''

import turtle
import os
os.chdir(r"C:\Users\olatunem\OneDrive - Seton Hall University\Extraneous\PYTHON WORKSPACE")

grid_size = 10
bombs = [(3,1),(2,6),(1,7),(6,2),(5,3),(4,4),(3,5),(10,6)]
start = (1,1)
end = (grid_size,grid_size)
path = [start]
visited = []
for i in bombs:
    visited.append(i)

#Algorithm
def find_path(loq,path,visited):
    if loq[0] == end[0] and loq[1] == end[1]:
        return path
    if loq[0]+1 <= grid_size and ((loq[0]+1,loq[1]) not in visited):
        loq = (loq[0]+1,loq[1])
        path.append(loq)
        visited.append(loq)
        return find_path(loq,path,visited)
    if loq[1]+1 <= grid_size and ((loq[0],loq[1]+1) not in visited):
        loq = (loq[0],loq[1]+1)
        path.append(loq)
        visited.append(loq)
        return find_path(loq,path,visited)
    else:
        if len(path) - 2 >= 0:
            path.remove(loq)
            loq = path[len(path)-1]
            return find_path(loq,path,visited)
        else:
            return 'No Path!'

def draw():
    #Screen
    wn = turtle.Screen()
    wn.bgcolor('white')
    wn.title('Robot Path')
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
    border_pen.setposition(-300,-300)
    gap = 600/grid_size
    for i in range(grid_size//2):
        border_pen.fd(gap)
        border_pen.lt(90)
        border_pen.fd(600)
        border_pen.rt(90)
        border_pen.fd(gap)
        border_pen.rt(90)
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.lt(90)
    for i in range(grid_size//2):
        border_pen.fd(gap)
        border_pen.lt(90)
        border_pen.fd(600)
        border_pen.rt(90)
        border_pen.fd(gap)
        border_pen.rt(90)
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    #No Path Message
    wn.addshape('nopath.gif')
    gam = turtle.Turtle()
    gam.shape('nopath.gif')
    gam.penup()
    gam.speed(10)
    gam_shift = 5
    gam.setposition(-290,0)
    gam.hideturtle()

    #Make Robot
    robot = turtle.Turtle()
    robot.shape('square')
    robot.speed(0)
    robot.penup()
    gap = (600/grid_size)/2
    robot.setposition(-300+gap,300-gap)
    robot.pendown()

    #Make Bombs
    bomb = turtle.Turtle()
    bomb.shape('circle')
    bomb.speed(0)
    bomb.penup()
    bomb.color('red','red')
    for i in bombs:
        x = -300 + (gap * ((i[0]*2)-1))
        y = 300 - (gap * ((i[1]*2)-1)) - (gap/3)
        bomb.setposition(x,y)
        bomb.begin_fill()
        bomb.circle(gap/2)
        bomb.end_fill()
    bomb.hideturtle()

    #Move Robot
    find_path(start,path,visited)
    print(path)
    for i in path:
        x = -300 + (gap * ((i[0]*2)-1))
        y = 300 - (gap * ((i[1]*2)-1))
        robot.setposition(x,y)
    #No Path Message
    x = -300 + (gap * ((grid_size*2)-1))
    y = 300 - (gap * ((grid_size*2)-1))
    if robot.xcor() != x and robot.ycor() != y:
        print('NO PATH!')
        while True:
            gam.showturtle()
            x = gam.xcor()
            x += gam_shift
            if x >= 292:
                gam_shift *= -1
            if x <= -292:
                gam_shift *= -1
            gam.setx(x)

    input('Enter any key to end program: ')

draw()
#print(find_path(start,path,visited))
