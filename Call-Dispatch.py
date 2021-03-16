'''
Call Center: Imagine you have a call center with three levels of employees:
respondent, manager, and director. An incoming telephone call must be first
 allocated to a respondent who is free. If the respondent can't handle the 
 call, he or she must escalate the call to a manager. If the manager is not 
 free or not able to handle it, then the call should be escalated to a 
 director. Design the classes and data structures for this problem. 
 Implement a method dispatchCall() which assigns a call to the first 
 available employee. '''

import threading

class Call_Center:
    def __init__(self,name):
        self.__name = name
        self.__employees = []

    def main(self):
        a = input('Enter "call" to call: ')
        if a == 'call':
            self.dispatchCall()
            self.main()
        else:
            print('You entered an un-recognized command')
            self.main()

    def employ(self,fname,lname,title):
        if title == 'Respondent':
            self.__employees.append(Respondent(fname,lname,title))
        if title == 'Manager':
            self.__employees.append(Manager(fname,lname,title))
        if title == 'Director':
            self.__employees.append(Director(fname,lname,title))

    def dispatchCall(self):
        respondents = []
        managers = []
        directors = []
        full_status = []
        for i in self.__employees:
            if i.gettitle() == 'Respondent':
                respondents.append(i)
            if i.gettitle() == 'Manager':
                managers.append(i)
            if i.gettitle() == 'Director':
                directors.append(i)
            full_status.append(i.call_status())
        if False not in full_status:
            print('Please hold and the next available employee will get to you shortly!')
            timer = threading.Timer(10.0,self.dispatchCall)
            timer.start()
        search = True                
        for i in respondents:
            if search == True and i.call_status() == False:
                i.assigncall()
                i.settimer(threading.Timer(15.0,i.endcall))
                i.starttimer()
                search = False
                print('Respondent,',i.fname(),i.lname(),'has been assigned the call!')
        for i in managers:
            if search == True and i.call_status() == False:
                i.assigncall()
                i.settimer(threading.Timer(15.0,i.endcall))
                i.starttimer()
                search = False
                print('Manager,',i.fname(),i.lname(),'has been assigned the call!')
        for i in directors:
            if search == True and i.call_status() == False:
                i.assigncall()
                i.settimer(threading.Timer(15.0,i.endcall))
                i.starttimer()
                search = False
                print('Director,',i.fname(),i.lname(),'has been assigned the call!')

class Employee:
    def __init__(self,fname,lname):
        self.__fname = fname
        self.__lname = lname
        self.__call_status = False
        self.__timer = None

    def assigncall(self):
        self.__call_status = True

    def endcall(self):
        self.__call_status = False
        print(self.__fname,self.__lname,'is available for call')

    def call_status(self):
        return self.__call_status

    def settimer(self,time):
        self.__timer = time

    def starttimer(self):
        self.__timer.start()

    def fname(self):
        return self.__fname

    def lname(self):
        return self.__lname

class Respondent(Employee):
    def __init__(self,fn,ln,t):
        self.__title = t
        Employee.__init__(self,fn,ln)

    def gettitle(self):
        return self.__title

class Manager(Employee):
    def __init__(self,fn,ln,t):
        self.__title = t
        Employee.__init__(self,fn,ln)

    def gettitle(self):
        return self.__title

class Director(Employee):
    def __init__(self,fn,ln,t):
        self.__title = t
        Employee.__init__(self,fn,ln)

    def gettitle(self):
        return self.__title

#################################################################################
Center1 = Call_Center('Africell')
Center1.employ('Emmanuel','Olatunde','Director')
Center1.employ('Joseph','Scelera','Manager')
Center1.employ('Marco','Morazan','Manager')
Center1.employ('Femi','Adebonye','Respondent')
Center1.employ('Moses','Olatunde','Respondent')
Center1.employ('Gabriel','Olatunde','Respondent')

Center1.main()



