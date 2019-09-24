# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:18:52 2019

@author: ck186026
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert_node(self, newnode):
        if self.head == None and self.tail == None:
            self.head = newnode
            self.tail = newnode
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp
            self.tail = newnode
        self.length += 1

    def insert_at_beg(self, newnode):
        if self.head == None and self.tail == None:
            self.insert_node(newnode)
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            self.length += 1
    
    def insert_at_last(self, newnode):
        if self.head == None and self.tail == None:
            self.insert_node(newnode)
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
            self.length += 1

    def insert_at_pos(self, newnode, pos):
        count = 1
        temp = self.head
        if pos > self.length+1:
            print("Number of nodes in dll is lessthan the given position")
            return
        if pos == 1:
            self.insert_at_beg(newnode)
            return
        elif pos == self.length + 1:
            self.insert_at_last(newnode)
            #return
        else:
            while temp != None and count <= pos:
                if count == pos:
                    temp.prev.next = newnode
                    newnode.prev = temp.prev
                    newnode.next = temp
                    temp.prev = newnode
                    self.length += 1
                    print("Hi")
                    return
                    
                else:
                    temp = temp.next
                    count += 1

    def delete_beg(self):
        if self.head == None:
            print("The dll is empty")
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1

    def delete_last(self):
        if self.tail == None:
            print("The dll is empty")
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
    
    def delete_at_pos(self, pos):
        count = 1
        temp = self.head
        if pos == 1:
            self.delete_beg()
        elif pos == self.length:
            self.delete_last()
        else:
            while temp != None and count <= pos:
                if count == pos:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return
                else:
                    temp = temp.next
                    count += 1
        
 
    def fwdprint(self):
        print("Forward priniting of the nodes")
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def revprint(self):
        print("Reverse priniting of the nodes")
        temp = self.tail
        while(temp):
            print(temp.data)
            temp = temp.prev

if __name__ == '__main__':
    dlinkedlist = DoubleLinkedList()
    dlinkedlist.insert_node(Node(1))
    dlinkedlist.insert_node(Node(2))     
#    dlinkedlist.insert_node(Node(3))
    dlinkedlist.insert_at_beg(Node(0))
    dlinkedlist.insert_at_last(Node(4))
    dlinkedlist.insert_at_pos(Node(3), 5)    
    dlinkedlist.delete_beg()
    dlinkedlist.delete_last()
    dlinkedlist.delete_at_pos(2)
    dlinkedlist.fwdprint()
    dlinkedlist.revprint()