from list import LinkedList, Node

list = LinkedList()

list.insertAtBeginning("primeiro elemento")
list.insertAtEnd("segundo elemento")
list.insertAtBeginning("terceiro elemento")
list.insertAtGivinPosition(1, "quarto elemento")
list.deleteAtPosition(2)
list.deleteFromEnd()
list.printLinkedList()