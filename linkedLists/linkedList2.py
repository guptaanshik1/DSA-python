class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def printSLL(self):
        if self.head is None:
            print("The linked list does not exist")
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next#when any node's next will reference None loop will stop

    # def createNode(self, nodeValue):
    #     if head

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
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
                #newNode.next = tempNode.next
                #tempNode.next = newNode


    def searchSLL(self, value):
        if self.head is None:
            return "The linked list does not exists"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == value:
                    return value
                tempNode = tempNode.next
        return "The value does not exists in the linked list"

    def deleteNode(self, location):
        if self.head is None:
            print("The linked list does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:#when tempNode will reference the node which is reference by tail
                            break
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:#one node behind the node which has to be deleted
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next#the node after the deleted node
                    
    def deleteEntireSLL(self):
        if self.head is None:
            print("The linked list does not exist")
        else:
            self.head = None
            self.tail = None
            print("The entire linked list is deleted")

def createNode(ll, nodeValue):
    firstNode = Node(nodeValue)
    ll.head = firstNode
    ll.tail = firstNode
    firstNode.next = None
    return ll.head

def insertSLLRec(head, nodeValue):
    newNode = Node(nodeValue)
    if head is not None:
        head.next = insertSLLRec(head.next, nodeValue)
        return head
    else:
        head = newNode
        return head

singlyLinkedList = SLinkedList()
head = createNode(singlyLinkedList, 1)
insertSLLRec(head, 2)
insertSLLRec(head, 2)
# insertSLLRec(singlyLinkedList, 3)
# insertSLLRec(singlyLinkedList, 4)
# insertSLLRec(singlyLinkedList, 6)
# node1 = Node(1)
# node2 = Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2

# nodeValue = int(input("Enter a value to be added to a node: "))
# location = int(input("Enter the location of the node: "))

# singlyLinkedList.insertSLL(nodeValue, location)



# singlyLinkedList.insertSLL(2, -1)
# singlyLinkedList.insertSLL(3, -1)
# singlyLinkedList.insertSLL(4, -1)
# singlyLinkedList.insertSLL(0, 0)
# singlyLinkedList.insertSLL(6, 2)
# singlyLinkedList.insertSLL(-1, 1)

singlyLinkedList.printSLL()

# print()

# print(singlyLinkedList.searchSLL(1))

# print()

# singlyLinkedList.deleteNode(2)
# singlyLinkedList.printSLL()
