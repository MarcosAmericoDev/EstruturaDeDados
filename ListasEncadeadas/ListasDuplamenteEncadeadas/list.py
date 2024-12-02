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
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            newNode.prev = current
            newNode.next = None
        self.length += 1