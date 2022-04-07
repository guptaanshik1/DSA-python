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
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        print("The node has been created")

    def traverseDLL(self):
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

    def insertNode(self, NodeValue, location):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            newNode = Node(NodeValue)
            if location == 0:
                newNode.prev = None
                self.head.prev = newNode#2nd node with newNode(reverse link)
                newNode.next = self.head#newNode with 2nd link(forward link)
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode#second last node with newNode(forward link)
                newNode.prev = self.tail#newNode with second last node(reverse link)
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next#newNode with nextNode(forward link)
                newNode.next.prev = newNode#newNode with nextNode(reverse link)
                tempNode.next = newNode#currentNode with newNode(forward link)
                newNode.prev = tempNode#curentNode with newNode(reverse link)

    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the linked list"
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
                    self.head = self.head.next#head with second Node
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev.next = None#last node's prev's next i.e second last node's next to None
                    self.tail = self.tail.prev#tail with prev's reference of last node i.e second last node

                    # self.tail = self.tail.prev
                    # self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next#currentNode with the node after the node to be deleted(forward link)
                tempNode.next.prev = tempNode#currentNode with the node after the node to be deleted(reverse link)

    def deleteEntireDLL(self):
        if self.head is None:
            print("There is node in the doubly linked list")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None#each node's prev reference with null
                tempNode = tempNode.next
            self.head = None
            self.tail = None

doublyLL = DoublyLinkedList()

doublyLL.createNode(1)

doublyLL.insertNode(0, 0)
doublyLL.insertNode(2, -1)
doublyLL.insertNode(4, 2)
doublyLL.insertNode(3, 1)

doublyLL.traverseDLL()
print()

doublyLL.reverseTraversalDLL()
print()

print(doublyLL.searchDLL(4))
print(doublyLL.searchDLL(10))

doublyLL.deleteNode(2)
print()

doublyLL.traverseDLL()
print()

doublyLL.deleteEntireDLL()

doublyLL.traverseDLL()