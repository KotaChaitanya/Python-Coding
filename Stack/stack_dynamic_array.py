class Stack:
    def __init__(self,limit=10):
        self.stk=[]
        self.limit=limit
        
    def isEmpty(self):
        return len(self.stk) <=0
    def push(self,item):
        if(len(self.stk) >= self.limit):
            self.resize()
        self.stk.append(item)
        print("After insert Stack= " , self.stk)
    def pop(self):
        if(len(self.stk) <=0):
            print("Stack Underflow")
            return 0
        else:
            return self.stk.pop()
    def size(self):
        return len(self.stk)
    def peek(self):
        if(len(self.stk) <=0):
            print("Stack Underflow")
            return 0
        else:
            return self.stk[-1]
    def resize(self):
        newStk=list(self.stk)
        self.limit=2*self.limit
        self.stk=newStk

#Main Code
my_stack=Stack(1)
my_stack.push(1)
my_stack.push(12)
print(str(my_stack.pop()) + " is poped from stack")
my_stack.push(15)
print(str(my_stack.peek()) + " is top ele")
