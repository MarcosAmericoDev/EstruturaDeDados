class Stack:
    def __init__(self, Capacity=1):
        self.top = -1
        self.Capacity = Capacity
        self.A = [None]*Capacity
    
    def push(self, data):
        if self.top == self.Capacity - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.A[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflox")
            return
        valueInStackPosition = self.A[self.top]
        self.A[self.top] = None
        self.top -= 1
        return valueInStackPosition
    
    def peek(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        return self.A[self.top]
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.Capacity-1
    
    def printStack(self):
        for item in self.A:
            print(item) 