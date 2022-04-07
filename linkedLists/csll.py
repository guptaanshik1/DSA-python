class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createCSLL(self, nodeValue):
        firstNode = Node(nodeValue)
        firstNode.next = firstNode
        self.head = firstNode
        self.tail = firstNode

    def traversalCSLL(self):
        if self.head is None:
            print("There is no node in the linked list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def insertCSLL(self, nodeValue, location):
        newNode = Node(nodeValue)
        if self.head is None:
            print("The Circular Single Linked List does not exist")
        else:
            if location == 0:
                newNode.next = self.head#newNode linked with previously first node
                self.head = newNode
                self.tail.next = newNode#last node linked with first node
            elif location == -1:
                newNode.next = self.tail.next#tail.next is the previously last node and it references to the first node
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the linked list"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node is not present in the linked list"

    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in the linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    self.head = self.head.next#head and second node
                    self.tail.next = self.head#last node with second node
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    self.tail = tempNode
                    tempNode.next = self.head
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next#nextNode is the node to be deleted
                tempNode.next = nextNode.next

    def deleteEntireCSLL(self):
        if self.head is None:
            print("There is no node in the linked list")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None
            print("The linked list is deleted successfully")
                    
circularSLL = CircularSinglyLinkedList()

circularSLL.createCSLL(1)
circularSLL.insertCSLL(2, -1)
circularSLL.insertCSLL(3, -1)
circularSLL.insertCSLL(4, -1)
circularSLL.insertCSLL(-1, 1)
circularSLL.insertCSLL(0, 0)

circularSLL.traversalCSLL()

print()

print(circularSLL.searchCSLL(4))
print(circularSLL.searchCSLL(10))

circularSLL.deleteNode(10)

print()

circularSLL.traversalCSLL()

print()

circularSLL.deleteEntireCSLL()

circularSLL.traversalCSLL()