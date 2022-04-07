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
        firstNode.next = firstNode
        firstNode.prev = firstNode
        self.head = firstNode
        self.tail = firstNode
        print("The node has been created successfully")

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
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the circular doubly linked list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value ==  nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The node does not exist in the circular doubly linked list"
                tempNode = tempNode.next

    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in the linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    newNode.next = None
                    newNode.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    newNode.next = None
                    newNode.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode
            
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

circularDLL = CircularDoublyLinkedList()

circularDLL.createNode(1)
circularDLL.insertNode(0, 0)
circularDLL.insertNode(2, -1)
circularDLL.insertNode(3, -1)
circularDLL.insertNode(-1, 1)
circularDLL.insertNode(-2, 3)

circularDLL.traverseCDLL()
print()

circularDLL.reverseTraversalCDLL()
print()

print(circularDLL.searchCDLL(2))
print(circularDLL.searchCDLL(10))

circularDLL.deleteNode(-1)
print()

circularDLL.traverseCDLL()
print()

circularDLL.deleteEntireCDLL()
circularDLL.traverseCDLL()