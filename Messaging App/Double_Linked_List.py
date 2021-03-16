import string as string

class Node:
    #Node: data Node
    def __init__(self,data,blink,link):
        self._data = data
        self._link = link
        self._blink = blink
    
    #To get the data in a node
    def get_data(self):
        return self._data
    
    #To mutate the data in a node
    def change_data(self, data):
        self._data = data
    
    #To get node that is linked to this node
    def get_link(self):
        return self._link
    
    #To mutate the node that is linked to this node
    def change_link(self, link):
        self._link = link
    
    #To get node that is linked to this node
    def get_blink(self):
        return self._blink
    
    #To mutate the node that is linked to this node
    def change_blink(self, link):
        self._blink = link
############################################################################################
class DoubleLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None        
    
    def get_head(self):
        return self._head

    #To make the given node the head
    def insert_head(self, node):
        if self._head == None:
            self._head = node
        else:
            self._head.change_blink(node)
            node.change_link(self._head)
            self._head = node
    
    #To get the last node in the Linked List
    #   To help the insert_tail function
    def get_last(self):
        Done = False
        node = self._head
        while Done is not True:
            if node.get_link() == self._tail:
                Done = True
                return node
            else:
                node = node.get_link()

    #To make the given node the tail of the DoubleLinkedList       
    def insert_tail(self, node):
        node.change_link(self._tail)
        node.change_blink(self.get_last())
        self.get_last().change_link(node)
    
    #To remove node at head of the DoubleLinkedList
    def remove_head(self):
        self._head = self._head.get_link()
    
    #To remove node at tail of DoubleLinkedList
    def remove_tail(self):
        self.get_last().get_blink().change_link(self._tail)
        
    #To Print out all the nodes in the DoubleLinkedList
    def printl(self, node):
        if (node != None):
            print(node.get_data())
            self.printl(node.get_link())

    #To mutate the data in the head node
    def change_head(self,data):
        self._head.change_data(data)

    #To mutate the data in the tail node
    def change_tail(self,data):
        self.get_last().change_data(data)

    #To compute if a node-data is in the DoubleLinkedList
    def search(self,node,key):
        if (node != None and node.get_data() == key):
            return True
        elif(node != None and node.get_link() != None):
            return self.search(node.get_link(),key)
        else:
            return False

    #Remove from Head
    def remove_enhanced(self,data):
        if self.search(self._head,data) == True:
            node = self._head
            if self._head.get_data() == data:
                self.remove_head()
            else:
                k = True
                while k != False and node.get_link() != None:
                    if node.get_link().get_data() == data:
                        node.change_link(node.get_link().get_link())
                        k = False
                    else:
                        node = node.get_link()
        else:
            print(data,' does not exist in Linked List')

    #Reverse LinkedList
    def reverse(self):
        prev = None
        current = self._head
        while current is not None:
            next = current.get_link()
            current.change_link(prev)
            prev = current
            current = next
        self._head = prev

    def empty(self):
        self._head = None

        
##################################################################################




        
    

