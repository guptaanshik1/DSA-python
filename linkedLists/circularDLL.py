class Node:
    def __init__(self, value = None):
        self.value = value
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def createNode(self, nodeValue):
        firstNode = Node(nodeValue)
        self.head = firstNode
        self.tail = firstNode
        firstNode.next = firstNode
        firstNode.prev = firstNode
        print("The node has been created")

    def traverseCDLL(self):
        if self.head is None:
            print("There is no node in the circular doubly linked list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    def reverseTraversalCDLL(self):
        if self.head is None:
            print("There is no node in the circular doubly linked list")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("There is no node in the circular doubly linked list")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head#newNode with previously first Node(fowrward link)
                newNode.prev = self.tail#new with last node
                self.head.prev = newNode#previously first node with newNode(reverse link)
                self.head = newNode
                self.tail.next = newNode#newNode with last node
            elif location == -1:
                newNode.next = self.head#newNode with first node
                newNode.prev = self.tail#newNode with previously last node(reverse link)
                self.head.prev = newNode#first node with last node
                self.tail.next = newNode#previously last node with newNode(forward link)
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next#newNode with afterNode(forward link)
                newNode.prev = tempNode#newNode with beforeNode(reverse link)
                newNode.next.prev = newNode#newNode with afterNode(reverse link)
                tempNode.next = newNode#newNode with beforeNode(forward link)

    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the circular doubly linked list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next
            return "The node does not exixt in the circular doubly linked list"

    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in the circular doubly linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next#head with second node
                    self.head.prev = self.tail#second node with last node(reverse link)
                    self.tail.next = self.head#last node with second node(forward link)
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev#tail with second last node
                    self.tail.next = self.head#second last node with first node(forward link)
                    self.head.prev = self.tail#first node with second last node(reverse link)
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next#beforeNode with afterNode(forward link)
                tempNode.next.prev = tempNode#afterNode with beforeNode(reverse link)

    def deleteEntireCDLL(self):
        if self.head is None:
            print("There is no node in the circular doubly linked list")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The entire circular doubly linked list has been deleted")
        
circularDLL = CircularDoublyLinkedList()

circularDLL.createNode(1)

circularDLL.insertNode(0, 0)
circularDLL.insertNode(2, -1)
circularDLL.insertNode(3, -1)
circularDLL.insertNode(-1, 1)

circularDLL.traverseCDLL()
print()
circularDLL.reverseTraversalCDLL()
print()

print(circularDLL.searchCDLL(2))
print(circularDLL.searchCDLL(10))
print()

circularDLL.deleteNode(2)
circularDLL.traverseCDLL()

circularDLL.deleteEntireCDLL()
circularDLL.traverseCDLL()