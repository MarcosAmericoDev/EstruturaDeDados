class Stack:
    def __init__(self, Capacity=1):
        self.top = -1
        self.Capacity = Capacity
        self.A = [None]*Capacity

    def push(self, data):
        if self.top == self.Capacity - 1:
            self.Resize(1)
        self.top += 1
        self.A[self.top] = data
    
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return
        
        temp = self.A[self.top]
        self.A[self.top] = None
        self.top -= 1

        if self.top < self.Capacity // 2:
            self.Resize(0)

        return temp

    def Resize(self, dir):
        if dir == 1:
            self.Capacity = self.Capacity * 2
        else: 
            self.Capacity = self.Capacity // 2
        newArray = [None] * self.Capacity
        for i in range(0, self.top + 1):
            newArray[i] = self.A[i]

        self.A = newArray

    def printStack(self):
        for item in self.A:
            print(item) 