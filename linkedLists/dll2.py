class Node:
    def __init__(self, value = None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createNode(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        node.next = None
        node.prev = None
        print("The creation of Doubly linked list is successfull")

    def traversalDLL(self):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def reverseTraversalDLL(self):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def insertNodeDLL(self, nodeValue, location):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                self.head.prev = newNode
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.next.prev = newNode
                newNode.prev = tempNode
                tempNode.next = newNode

    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the doubly linked list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exists in the doubly linked list"

    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode                 

    def deleteEntireDLL(self):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None

doublyLL = DoublyLinkedList()

doublyLL.createNode(1)
doublyLL.insertNodeDLL(0, 0)
doublyLL.insertNodeDLL(2, -1)
doublyLL.insertNodeDLL(-1, 1)

doublyLL.traversalDLL()
print()

doublyLL.reverseTraversalDLL()
print()

print(doublyLL.searchDLL(-1))

print(doublyLL.searchDLL(10))

doublyLL.deleteNode(1)
print()

doublyLL.traversalDLL()

print()
doublyLL.deleteEntireDLL()

doublyLL.traversalDLL()