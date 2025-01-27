class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enQueue(self, data):
        node = QueueNode(data)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node
        
        self.size += 1
    def deQueue(self):
        if self.size > 0:
            elem = self.first.data
            self.first = self.first.next
            self.size -= 1
            return elem
        raise IndexError("The queue is empty")
    
    def queueFirst(self):
        if self.size > 0:
            return self.first.data
        raise IndexError("The queue is empty")
    
    def printQueue(self):
        current = self.first
        while current is not None:
            print(current.data)
            current = current.next

    def isEmpty(self):
        return self.size == 0
    
if __name__ == "__main__":
    fila = Queue()
    fila.enQueue(5)
    fila.enQueue("Robson")
    fila.enQueue("Robson")
    fila.enQueue("Robson")
    fila.enQueue("Robson")
    fila.printQueue()