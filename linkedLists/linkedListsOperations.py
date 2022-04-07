class Node:
    def __init__(self, value = None):
        self.value = value#the value coming from parameter
        self.next = None#There will be one node in the beginning

class SLinkedList:
    def __init__(self):
        #since no node in the beginning
        self.head = None
        self.tail = None

    #method to travserse and print linked lists values
    def traverseAndPrint(self):
        if self.head is None:
            print("The linked list does not exist")
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:#if the linked list is empty
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head#the node which was the first node before, was referenced by head
                #so newNode.next is now referenced by head
                self.head = newNode#physical location of newNode to head's reference
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode#the node which was previously referenced by tail, now is referenced by 
                #the newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                #running a loop till node after which the newNode has to be inserted
                while index < location - 1:
                    tempNode = tempNode.next#the node referenced by the next node of the current node
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def searchSLL(self, value):
        if self.head is None:
            return "The linked does not exist"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == value:
                    return value
                tempNode = tempNode.next
            return "The value does not exists in the linked list"

    def deleteNode(self, location):
        if self.head is None:
            print("The linked list does not exists")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next#the head reference previously was first node now
                    #the node to which the first node's next references
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next#the node referenced by the next node of the current node
                    index += 1
                nextNode = tempNode.next#next of current node
                tempNode.next = nextNode.next#means the node after the node which will be deleted


singlyLinkedList = SLinkedList()
#values to be inserted into nodes
# node1 = Node(1)
# node2 = Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2#this first node's next
# singlyLinkedList.tail = node2

# singlyLinkedList.traverseAndPrint()
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(-1, 0)
singlyLinkedList.insertSLL(-2, 0)
singlyLinkedList.insertSLL(0, 3)
singlyLinkedList.insertSLL(1, 4)

singlyLinkedList.traverseAndPrint()
print()
print(singlyLinkedList.searchSLL(3))

singlyLinkedList.deleteNode(4)
singlyLinkedList.deleteNode(3)
singlyLinkedList.traverseAndPrint()