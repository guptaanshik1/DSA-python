class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverseCSLL(self):
        if self.head is None:
            print("The circular linked list does not exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def createCSLL(self, nodeValue):
        firstNode = Node(nodeValue)
        firstNode.next = firstNode
        self.head = firstNode
        self.tail = firstNode

    def insertCSLL(self, nodeValue, location):
        newNode = Node(nodeValue)
        if self.head is None:
            print("There is no node in the circular linked list")
        else:
            if location == 0:
                newNode.next = self.head#1st node with 2nd node
                self.head = newNode
                self.tail.next = newNode#last node with 1st node
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next#the node after the node to be inserted
                tempNode.next = newNode#current node with the node to be inserted
                newNode.next = nextNode#the node to be inserted with the next node after the node to be inserted

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
                    return "The node does not found in the circular linked list"

    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in the circular linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
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
                nextNode = tempNode.next#the node to be deleted
                tempNode.next = nextNode.next
    
    def deleteEntireCSLL(self):
        if self.head is None:
            print("There is no node in the linkde list")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None

circularSLL = CircularSinglyLinkedList()

circularSLL.createCSLL(1)

circularSLL.insertCSLL(0, -1)
circularSLL.insertCSLL(10, -1)
circularSLL.insertCSLL(11, 1)
circularSLL.insertCSLL(1, 1)
circularSLL.insertCSLL(5, -1)

circularSLL.traverseCSLL()

print()

print(circularSLL.searchCSLL(5))

circularSLL.deleteNode(0)

print()
circularSLL.traverseCSLL()

print()

circularSLL.deleteEntireCSLL()

circularSLL.traverseCSLL()