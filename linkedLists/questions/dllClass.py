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
        firstNode = Node(nodeValue)
        firstNode.next = None
        firstNode.prev = None
        self.head = firstNode
        self.tail = firstNode
        # print("The node has been created successfully")

    def traverseDLL(self):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def reverseTraverseDLL(self):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = None
                # newNode.next.prev = newNode
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                newNode.next = None
                newNode.prev = self.tail
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

    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the doubly linked list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does exist in the doubly linked list"

    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in the doubly linked list")
        else:
            if location == 0:
                self.head = self.head.next
                self.head.prev = None
            elif location == -1:
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

    def insert(self, nodeValue):
        newNode = Node(nodeValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def lengthList(self):
        if self.head is None:
            print("There is no node in the single linked list")
        else:
            res = 0
            tempNode = self.head
            while tempNode:
                res += 1
                tempNode = tempNode.next
            return res

    def nthToLast(self, value):
        pointer1 = self.head
        pointer2 = self.head

        for i in range(value):#for creating gap of values between the pointers
            if pointer2 is None:
                return None
            pointer2 = pointer2.next

        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1.value

def sumList(ll1, ll2):
    tempLL1 = ll1.head
    tempLL2 = ll2.head
    carry = 0
    ll = DoublyLinkedList()
    while tempLL1 or tempLL2:
        result = carry
        if tempLL1 is not None:
            result += tempLL1.value
            tempLL1 = tempLL1.next
        if tempLL2 is not None:
            result += tempLL2.value
            tempLL2 = tempLL2.next
        # if tempLL1 == ll1.tail:
        #     break
        ll.insert(int(result % 10))#1's digit
        carry = result / 10#10's digit
    return ll.traverseDLL()

def intersection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        print("false")

    len1 = ll1.lengthList()
    len2 = ll2.lengthList()
    # print()
    # print(len1)
    # print()
    # print(len2)

    shorter = ll1 if len1 < len2 else ll2#shorter is ll1 if len1 is shorter
    longer = ll2 if len1 < len2 else ll1#longer is ll2 if len1 is shorter
    print()
    shorter.traverseDLL()
    print()
    longer.traverseDLL()
    print()

    extraNode = longer.lengthList() - shorter.lengthList()
    print(extraNode)

    shorterNode = shorter.head
    longerNode = longer.head

    # print("shorterNode", shorterNode.value)
    # print("longerNode", longerNode.value)

    for i in range(extraNode):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        if shorterNode.value == longerNode.value:
            break
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode.value

doublyLL = DoublyLinkedList()

doublyLL.createNode(1)
doublyLL.insertNode(0, 0)
doublyLL.insertNode(2, -1)
doublyLL.insertNode(3, -1)
doublyLL.insertNode(-1, 1)
doublyLL.insertNode(-2, 3)

doublyLL.traverseDLL()
print()

# doublyLL.reverseTraverseDLL()
print()

# print(doublyLL.searchDLL(1))
# print(doublyLL.searchDLL(10))

print()

# doublyLL.deleteNode(1)

# doublyLL.traverseDLL()
# print()

print(doublyLL.nthToLast(4))

print("------------------------------------")

doublyLL1 = DoublyLinkedList()
doublyLL2 = DoublyLinkedList()

doublyLL1.createNode(7)
doublyLL1.insertNode(1, -1)
doublyLL1.insertNode(6, -1)
doublyLL1.insertNode(8, -1)
doublyLL1.insertNode(10, -1)
doublyLL1.insertNode(12, -1)
# doublyLL1.traverseDLL()
print()

doublyLL2.createNode(5)
doublyLL2.insertNode(9, -1)
doublyLL2.insertNode(2, -1)
doublyLL2.insertNode(10, -1)
doublyLL2.insertNode(12, -1)
# doublyLL2.traverseDLL()
print()
# sumList(doublyLL1, doublyLL2)

print(intersection(doublyLL1, doublyLL2))