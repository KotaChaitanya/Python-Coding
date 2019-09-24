class Node:
    def __init__(self):
        self.data = None
        self.next = None
    #method for setting the data field of the node
    def set_data(self,data):
        self.data = data
    #method for setting the next field of the node
    def set_next(self,next):
        self.next = next
    #method for getting the data field of the node
    def get_data(self):
        return self.data
    #method for getting the next field of the node
    def get_next(self):
        return self.next
    #return true if the node points to another node
    def hasNext(self):
        return self.next!=None

class Queue:
    #constructor
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    #method for enQueueing element to stack
    def enQueue(self,data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(None)
        if self.rear == None and self.front == None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp
        self.length += 1
        
        print("Queue after Enqueue = ", end = "")
        self.display()

    #method to deQueue element from stack
    def deQueue(self):
        if self.front == None:
            print("Queue is underflow")
            return
        else:
            self.front = self.front.next
            self.length -= 1
        print("Queue after Dequeue = ", end = "" )
        self.display()
    #method to display contents of a stack
    def display(self):
        temp = self.front
        if temp:
            while(temp.next):
                print(temp.data, end= " -> ")
                temp = temp.next
            print(temp.data)
        else:
            print("Queue is empty")
    #method to return size of stack
    def size(self):
        return self.length
    #method to get the top element in the stack
    def peek(self):
        if self.front:
            return self.front.data
    #method to check stack is empty or not
    def isempty(self):
        return self.front == self.rear == None

#main code
s = Queue()
s.enQueue(1)
s.enQueue(2)
s.enQueue(3)
s.deQueue()
s.enQueue(4)
s.deQueue()
s.deQueue()
s.deQueue()
s.deQueue()
s.peek()
print(s.isempty())
print("Size of Queue: ", s.size())