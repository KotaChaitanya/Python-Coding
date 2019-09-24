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

class Stack:
    #constructor
    def __init__(self):
        self.head = None
        self.length = 0
    #method for pushing element to stack
    def push(self,data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head = temp
        self.length += 1
    #method to pop element from stack
    def pop(self):
        data = self.head.data
        self.head = self.head.next
        self.length -= 1
        return data
    #method to display contents of a stack
    def display(self):
        if self.head == None:
            print("Stack is empty")
        else:
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next
    #method to return size of stack
    def size(self):
        return self.length
    #method to get the top element in the stack
    def peek(self):
        return self.head.data
    #method to check stack is empty or not
    def isempty(self):
        return self.head == None

#main code
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Popped element is :", s.pop())
s.push(4)
print("Top element in the stack is :",s.peek())
s.display()
print(s.isempty())
print("Size of stack: ", s.size())