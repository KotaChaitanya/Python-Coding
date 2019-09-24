# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:02:24 2019

@author: ck186026
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    def set_next(self,nextadd):
        self.next = nextadd

class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert_node(self, newnode):
        if self.head == None and self.tail == None:
            self.head = newnode
            self.tail = newnode
            newnode.set_next(self.head)
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = newnode
            newnode.set_next(self.head)
            self.tail = newnode

        self.length += 1

    def insert_at_beg(self, newnode):
        if self.head == None and self.tail == None:
            self.insert_node(newnode)
        else:
            newnode.set_next(self.head)
            self.head = newnode
            self.tail.next = newnode
            self.length += 1

    def insert_at_last(self, newnode):
        if self.head == None and self.tail == None:
            self.insert_node(newnode)
        else:
            self.tail.next = newnode
            newnode.set_next(self.head)
            self.tail = newnode
            self.length += 1

    def insert_at_pos(self, newnode, pos):
        count = 1
        temp = self.head
        prev = None
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
                    newnode.next = temp
                    prev.next = newnode                 
                    self.length += 1
                    return                   
                else:
                    prev = temp
                    temp = temp.next
                    count += 1

    def delete_beg(self):
        if self.head == None:
            print("The cll is empty")
        else:
            self.head = self.head.next
            lastnode = self.tail
            lastnode.set_next(self.head)
            self.length -= 1

    def delete_last(self):
        if self.tail == None:
            print("The cll is empty")
        else:
            temp = self.head
            while(temp.next!= self.tail):
                temp = temp.next
            temp.set_next(self.head)
            self.tail = temp
            self.length -= 1            

    def delete_at_pos(self, pos):
        count = 1
        prev = None
        temp = self.head
        if pos == 1:
            self.delete_beg()
        elif pos == self.length:
            self.delete_last()
        else:
            while temp != None and count <= pos:
                if count == pos:
                    prev.set_next(temp.next)
                    self.length -= 1
                    return
                else:
                    prev = temp
                    temp = temp.next
                    count += 1

    def print_nodes(self):
        temp = self.head
        while(temp.next != self.head):
            print(temp.data)
            temp = temp.next
        print(temp.data)

if __name__ == '__main__':
    clinkedlist = CircularLinkedList()
    clinkedlist.insert_node(Node(1))
    clinkedlist.insert_node(Node(2))
    clinkedlist.insert_at_beg(Node(0))
    clinkedlist.insert_at_last(Node(4))
    clinkedlist.insert_at_pos(Node(3),4)
    clinkedlist.delete_beg()
    clinkedlist.delete_last()
    clinkedlist.delete_at_pos(3)
    clinkedlist.print_nodes()
#    dlinkedlist.insert_node(Node(3))