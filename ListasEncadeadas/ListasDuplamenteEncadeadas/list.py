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
        self.length += 1
    
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data

        if(self.head == None):
            self.head = self.tail = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            newNode.prev = self.tail
            newNode.next = None
            self.tail.next = newNode
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
            current.prev.next = newNode
            newNode.prev = current.prev
            current.prev = newNode
            newNode.next = current
        self.length += 1
    
    def deleteAtBeginning(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
    
    def deleteAtEnd(self):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1

    def deleteAtPosition(self, positionToDelete):
        if self.length == 0:
            return
        elif positionToDelete < 0 or positionToDelete > self.length:
            return
        elif positionToDelete == 0:
            self.deleteAtBeginning()
            return
        elif positionToDelete == self.length:
            self.deleteAtEnd()
            return
        count = 0
        currentNode = self.head #Poderia fazer com o tail, porém seria de trás para frente
        while count < positionToDelete:
            currentNode = currentNode.next
            count += 1
        currentNode.prev.next = currentNode.next
        self.length -= 1

    def printDoubleLinkedList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next