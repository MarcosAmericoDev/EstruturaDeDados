class Node():
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList():
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.data = data

        if(self.head == None):
            self.head = self.tail = newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data

        if(self.head == None):
            self.head = self.tail = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            newNode.prev = current
            newNode.next = None
            self.tail = newNode
        self.length += 1
    
    def insertAtPosition(self, data, positionToInsert):
        newNode = Node()
        newNode.data = data
        
        if positionToInsert < 0 or positionToInsert > self.length:
            return
        elif self.head == None or positionToInsert == 0:
            self.insertAtBeginning()
        elif positionToInsert == self.length:
            self.insertAtEnd()
        else:
            current = self.head
            count = 0
            while count < positionToInsert and current.next != None:
                current = current.next
                count += 1
            newNode.next = current.next
            newNode.prev = current
            current.next = newNode
            self.length += 1
