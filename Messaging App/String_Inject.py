import Double_Linked_List
from datetime import datetime
from tkinter import *
import tkinter
import os
import csv

window = Tk()
window.geometry('700x700')
window.title('String-Inject')
window.configure(bg = 'black')

frame = Frame(window, bg="olive")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

#Access to Data Handlers
#Puts data from souce into Linked-List
Data = Double_Linked_List.DoubleLinkedList()
try:
    os.chdir(r"C:\Users\olatunem\OneDrive - Seton Hall University\Extraneous\PYTHON WORKSPACE\Messaging App") 
    file1= open('Transcript.txt','r')
    c = 0
    w = ''
    for i in file1:
        w += i 
        c +=1 
        if c == 3:
            w = w[:len(w)-2]
            Data.insert_head(Double_Linked_List.Node(w,None,None))
            c = 0
            w = ''    
    Data.reverse() 
    file1.close()
except Exception:
    print('Transcript.txt not found')

logo = PhotoImage(file = 'Logo.png')
Logo = logo.subsample(3,3)
msg = Entry(frame)

#To add messages to LinkedList
def submit(user):
    global msg
    node = Double_Linked_List.Node(user+'\n'+str(msg.get())+'\n'+str(datetime.now()),None,None)
    Data.reverse()
    Data.insert_head(node)
    Data.reverse()
    for items in frame.winfo_children():
        if type(items) != tkinter.Canvas and type(items) != tkinter.Scrollbar:
            items.destroy()
    msg = Entry(frame)
    update()

#To generate text field to enter message
def text(user):
    global Data, msg
    l = Label(frame, text = user)
    l.place(x=4,y=390)
    msg.place(x=4,y=410,width= 550, height = 100)
    buttonAdd = Button(frame, text="Send", command=lambda a= user: submit(a))
    buttonAdd.place(x=4,y=515)   

#To update Interface with most recent message
def update():
    global Data, frame, msg
    node = Data.get_head()
    Person1 = 5
    Person2 = 350
    message_height = 10
    pmessage_height = 0
    while node != None:
        #To prevent interface overflow
        if message_height >= 376:
            message_height = 10
            pmessage_height = 0
            for items in frame.winfo_children():
                if type(items) != tkinter.Canvas and type(items) != tkinter.Scrollbar:
                    items.destroy()
        msg = Entry(frame)
        #Handle message allignment
        sms = Label(frame, text = node.get_data(), wraplength = 190, justify = LEFT)
        if node.get_data()[0:8] == 'Person 1':
            sms.place(x=Person1,y=message_height)
        if node.get_data()[0:8] == 'Person 2':
            sms.place(x=Person2,y=message_height)
        pmessage_height = sms.winfo_reqheight() + 10
        message_height += pmessage_height
        node = node.get_link()

#To save and stop messaging
def exit():
    global Data    
    try:
        file1= open('Transcript.txt','w',encoding='utf-8')
        node = Data.get_head()
        while node != None:
            file1.write(node.get_data()+'\n')
            node = node.get_link()
        window.quit()
        file1.close()
    except Exception:
        print('Transcript.txt not found')

#To save and View all messages till now
def memory():
    try:
        file1= open('History.txt','w',encoding='utf-8')
        file2= open('Transcript.txt','w',encoding='utf-8')
        node = Data.get_head()
        while node != None:
            file1.write(node.get_data()+'\n')
            file2.write(node.get_data()+'\n')
            node = node.get_link()
        file1.close()
        os.system('start " " History.txt')
    except Exception:
        print('Unable to Open File containing History!')

#To Clear all Messages in history
def empty():
    Data.empty()
    memory()

#Buttons
buttonAdd = Button(window, text="Person 1", bg = 'palegreen', command=lambda a= 'Person 1': text(a))
buttonAdd.place(x=75,y=640)
buttonAdd = Button(window, text="Person 2", command=lambda a= 'Person 2': text(a), bg = 'palegreen')
buttonAdd.place(x=195,y=640)
buttonAdd = Button(window, text="History", command=memory, bg = 'palegreen')
buttonAdd.place(x=315,y=640)
buttonAdd = Button(window, text="Exit", command=exit, bg = 'palegreen')
buttonAdd.place(x=435,y=640)
buttonAdd = Button(window, text="Clear History", command=empty, bg = 'palegreen')
buttonAdd.place(x=555,y=640)
buttonAdd = Button(window, text="Clear History", image = Logo, command=memory, bg= 'black')
buttonAdd.place(x=250,y=5)

update()
mainloop()
