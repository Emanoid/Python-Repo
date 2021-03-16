from tkinter import *
import random
import os
import sys

window = Tk()
window.geometry('700x700')
window.title('MINESWEEPER')
data= []
n = 0
revealed = 0

#To count the bombs around each cell
def count(l):
    c = 0
    for i in l:
        if i == '*' or i/2 == 5:
            c += 1
    return c

#To place Bombs around cells
def placebombs():
    global data
    r = 0
    c = 0
    while r < n:
        R = [r-1,r,r+1]
        C = [c-1,c,c+1]
        L = []
        for i in R:
            for j in C:
                if i >= 0 and i < n and j >= 0 and j < n:
                    L.append(data[i][j])
        if data[r][c] != 10:
            data[r][c] = count(L)
            L = []
        if data[r][c] == 10:
            data[r][c] = '*'
        if c == n-1:
            r += 1
        c = (c+1) % n

#To build the Mine
def build():
    global data,revealed
    revealed = 0
    for i in range(n):
        data.append([])
    r = 1
    c = 0
    while r <= n:
        data[r-1].append(random.randint(5,10))       
        buttonAdd = Button(window, text="", command=lambda a=r, b=c: display(a,b))
        buttonAdd.grid(row= r, column= c)
        buttonAdd.config(height = 1, width = 2)
      
        if c == n-1:
            r += 1
        c = (c+1) % n
    placebombs()  

#To dig up a Mine
def display(r,c):
    global revealed
    if data[r-1][c] == '*':
        #Reveal box
        l = Label(window, text=data[r-1][c])
        l.grid(row= r, column= c)
        l.config(height = 1, width = 2)
        revealed += 1
        #Announce Death
        l = Label(window, text='You Died!!')
        l.place(x =20, y = 40)
        l.config(height = 5, width = 9)
    else:
        #Reveal box
        l = Label(window, text=data[r-1][c])
        l.grid(row= r, column= c)
        l.config(height = 1, width = 2)
        revealed += 1
        if ((n*n) - revealed) == count_total_bombs():
            #Announce Victory
            l = Label(window, text='You Have Won!!')
            l.place(x =20, y = 40)
            l.config(height = 5, width = 15)


def reveal(r,c):
    #Reveal box
    l = Label(window, text=data[r-1][c])
    l.grid(row= r, column= c)
    l.config(height = 1, width = 2)

def showall():
    #Reveal all boxes
    for i in range(1,n+1):
        for j in range(n):
            reveal(i,j)

def restart():
    os.chdir(r"C:\Users\olatunem\OneDrive - Seton Hall University\Extraneous\PYTHON WORKSPACE")
    window.quit()
    os.system('start " " MineSweeper.exe')

#Size of grid
n = 20
buttonAdd = Button(window, text="Cheat", command=showall)
buttonAdd.grid(row = n + 1, column = n + 2)
buttonAdd = Button(window, text="New-Game", command=restart)
buttonAdd.grid(row = n + 2, column = n + 2)

def count_total_bombs():
    global data
    c = 0
    for i in data:
        for j in i:
            if j == '*':
                c += 1
    return c

build()
mainloop()
