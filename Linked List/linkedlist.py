# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:38:54 2019

@author: ck186026
"""

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_node(self, newnode):
        if self.head == None:
            self.head = newnode
        else:
            current_node = self.head
            while(current_node.next != None):
                current_node = current_node.next
            current_node.next = newnode
        self.length += 1

    def insert_beg(self, newnode):
        if self.head == None:
            self.insert_node(newnode)
        else:
            newnode.next = self.head
            self.head = newnode
            self.length += 1

    def insert_last(self, newnode):
        temp = self.head
        if self.head == None:
            self.insert_node(newnode)
        else:
            while(temp.next != None):
                temp = temp.next
            temp.next = newnode
            self.length += 1

    def insert_after_value(self, value, newnode):
        temp = self.head
        while(temp != None):
            if temp.data == value:
                newnode.next = temp.next
                temp.next = newnode
                self.length += 1
                return
            else:
                temp = temp.next
    
    def insert_before_value(self, value, newnode):
        temp = self.head
        prev = None
        while(temp!= None):
            if temp.data == value:
                newnode.next = temp
                prev.next = newnode
                self.length += 1
                return
            else:
                prev = temp
                temp = temp.next

    def insert_at_given_pos(self, pos, newnode):
        count = 1
        temp = self.head
        prev = None
        if pos > self.length+1:
            print("Number of nodes in dll is lessthan the given position")
            return
        if pos == 1:
            self.insert_beg(newnode)
            return
        elif pos == self.length + 1:
            self.insert_last(newnode)
        else:
            while temp != None and count <= pos:
                if count == pos:
                    newnode.next = temp
                    prev.next = newnode
                    return
                else:
                    prev = temp
                    temp = temp.next
                    count += 1

    def delete_beg(self):
        if self.head == None:
            print("No elements in the list")
        else:
            self.head = self.head.next
            self.length -= 1

    def delete_last(self):
        temp = self.head
        prev = None
        if not temp:
            return
        else:
            while(temp.next!= None):
                prev = temp
                temp = temp.next
            prev.next = None
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
                    prev.next = temp.next
                    self.length -= 1
                    return
                else:
                    prev = temp
                    temp = temp.next
                    count += 1

    def print_nodes(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert_node(Node(1))
#    linkedlist.insert_node(Node(2))
    linkedlist.insert_node(Node(3))
#    linkedlist.insert_node(Node(4))
    linkedlist.insert_node(Node(5))
    linkedlist.insert_beg(Node(0))
    linkedlist.insert_last(Node(7))
    linkedlist.insert_after_value(5, Node(6))
    linkedlist.insert_before_value(5, Node(4))
    linkedlist.insert_at_given_pos(3, Node(2))
    linkedlist.delete_beg()
    linkedlist.delete_last()
    linkedlist.delete_at_pos(2)
    linkedlist.print_nodes()