import math
import os
import turtle 
import sys

life = True
bullet_state = 'not ready'
bullet_initial = 0
def main():
    global life, bullet_state, bullet_initial
    #Make Screen
    wn = turtle.Screen()
    wn.bgcolor('black')
    wn.title('Space Invaders')

    #Make Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color('white')
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pensize(3)
    border_pen.pendown()
    for i in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()

    #Make Player
    player = turtle.Turtle()
    player.color('blue')
    player.shape('triangle')
    player.penup()
    player.speed(0)
    player.setposition(0, -275)
    player.setheading(90)
    playershift = 15

    #Make Enemy
    enemy = turtle.Turtle()
    enemy.color('red')
    enemy.shape('circle')
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-290,290)
    enemy.shapesize(1.5,1.5)
    enemyshift = 2

    #Make Bullet
    bullet = turtle.Turtle()
    bullet.color('yellow')
    bullet.shape('triangle')
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(.5,.5)
    bullet.setposition(0,-310)
    bullet.hideturtle()
    bulletshift = 15

    #Move Player
    def moveleft():
        x = player.xcor()
        x -= playershift
        if x <= -290:
            x = -290
        player.setx(x)
        
    def moveright():
        x = player.xcor()
        x += playershift
        if x >= 290:
            x = 290
        player.setx(x)

    #Compute Collision
    def collision(a,b):
        x1 = a.xcor()
        x2 = b.xcor()
        y1 = a.ycor()
        y2 = b.ycor()
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return dist <= 15

    def shoot():
        global bullet_state, bullet_initial
        bullet_state = 'ready'
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
        bullet_initial = y

    #Temporary Life Count
    def pause():
        global life
        life = False

    #Keyboard Commands
    turtle.listen()
    turtle.onkey(moveleft,'Left')
    turtle.onkey(moveright, 'Right')
    turtle.onkey(pause, 'p')
    turtle.onkey(shoot, 'space')

    #Game Timeline
    while life == True:
        #Move Enemy
        x = enemy.xcor()
        x += enemyshift
        if x >= 290:
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            enemyshift *= -1
        if x <= -290:
            y = enemy.ycor()
            y -= 40
            enemy.sety(y)
            enemyshift *= -1    
        enemy.setx(x)

        #Move Bullet
        if bullet_state == 'ready' and bullet_initial <= 320:
            bullet_initial += bulletshift
            bullet.sety(bullet_initial)
        if bullet_initial > 300:
            bullet_state = 'not ready'
            bullet.hideturtle()
            
        #Check for collision
        if collision(player,enemy) == True:
            pause()
            print('You have been defeated')
            print('The game has ended')
        if collision(enemy,bullet) == True:
            enemy.setposition(-290,290)
            bullet.setposition(0,-310)
            bullet_state = 'not ready'
            enemyshift = abs(enemyshift)
main()
choice = input('Press any character to quit game: ')

