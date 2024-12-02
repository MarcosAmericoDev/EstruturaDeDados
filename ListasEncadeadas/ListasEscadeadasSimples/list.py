class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next
    
    def hasNext(self):
        return self.next != None
    
class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None
    
    def setHead(self, Node):
        self.head = Node
    
    def getHead(self):
        return self.head
    
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.data = data

        if (self.length == 0):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
    
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data
        if (self.length == 0):
            self.head = newNode
            self.length += 1
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = newNode
        self.length += 1

    def insertAtGivinPosition(self, positionToInsert, data):
        if positionToInsert > self.length or positionToInsert < 0:
            return None # Não faz sentido inserior onde a lista não cobre
        if positionToInsert == 0:
            self.insertAtBeginning(data)
            return
        if positionToInsert == self.length:
            self.insertAtEnd(data)
            return
        
        newNode = Node()
        newNode.data = data
        count = 1
        current = self.head

        while (count < positionToInsert-1):
            count += 1
            current = current.next

        newNode.next = current.next
        current.next = newNode
        self.length += 1
    
    def printLinkedList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
