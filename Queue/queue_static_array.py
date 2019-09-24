# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:04:55 2019

@author: ck186026
"""

class Queue:
    def __init__(self, limit = 10):
        self.queue = []
        self.limit = 10
        self.front = None
        self.rear = None
        self.size = 0
    def enQueue(self, data):
        if(self.size >= self.limit):
            print("Queue Overflow")
            return 0
        
        self.queue.append(data)
        
        if self.front == None and self.rear == None:
            self.front = self.rear = 0
        else:
            self.front = self.size

        self.size += 1
        print("After insert Queue= " , self.queue)

    def deQueue(self):
        if(self.size == 0):
            print("Queue Underflow")
            return 0
        else:
            self.queue.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
        print("Queue after Dequeue = " , self.queue)

    def queueRear(self):
        if self.rear is None:
            print("Sorry, the queue is empty!")
            raise IndexError
            return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            print("Sorry, the queue is empty!")
            raise IndexError
            return self.que[self.front]

    def peek(self):
        if(len(self.queue) <=0):
            print("Queue Underflow")
            return 0
        else:
            return self.queue[-1]        
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return len(self.queue) <=0    

#Main Code
my_queue=Queue(5)
my_queue.enQueue(1)
my_queue.enQueue(12)
print(str(my_queue.deQueue()) + " is deQueueed from stack")
my_queue.enQueue(15)
print(str(my_queue.peek()) + " is top ele")