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
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    
    def reverseTraversalCDLL(self):
        if self.head is None:
            print("There is no node in the circular doubly linked list")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
                if tempNode == self.tail:
                    break

    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("There is no node in the circular doubly linked list")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                self.head.prev = newNode
                newNode.prev = self.tail
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.prev = self.tail
                newNode.next = self.head
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
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail:
                    return "The node does not exist in the circular doubly linked list"

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
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
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

    def insert(self, nodeValue):
        newNode = Node(nodeValue)
        if self.head is None:
            self.head = newNode
            # self.tail = newNode
            newNode.next = newNode
            newNode.prev = newNode
            self.tail = newNode
        else:
            # self.tail.next = newNode
            # self.tail = self.tail.next
            # newNode.next = self.head
            newNode.next = self.head
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.head.prev = newNode

    def lengthList(self):
        if self.head is None:
            print("There is no node in the single linked list")
        else:
            res = 0
            tempNode = self.head
            while tempNode:
                if tempNode == self.tail:
                    break
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

        while pointer2 is not self.tail:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1.value
        
def sumList(ll1, ll2):
    tempLL1 = ll1.head
    tempLL2 = ll2.head
    carry = 0
    ll = CircularDoublyLinkedList()
    while tempLL1 or tempLL2:
        result = carry
        if tempLL1 is not None:
            result += tempLL1.value
            tempLL1 = tempLL1.next
        if tempLL2 is not None:
            result += tempLL2.value
            tempLL2 = tempLL2.next
        ll.insert(int(result % 10))#1's digit
        carry = result / 10#10's digit
        if tempLL2 == ll2.tail.next:
            break
    return ll.traverseCDLL()

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

print()

print(circularDLL.nthToLast(3))

# circularDLL.deleteNode(3)
# circularDLL.traverseCDLL()

# circularDLL.deleteEntireCDLL()
# circularDLL.traverseCDLL()
print("________________________________")

circularDLL1 = CircularDoublyLinkedList()
circularDLL2 = CircularDoublyLinkedList()

circularDLL1.insert(7)
circularDLL1.insert(1)
circularDLL1.insert(6)
circularDLL1.insert(8)
circularDLL1.insert(10)
circularDLL1.insert(12)
circularDLL1.traverseCDLL()

print()
circularDLL2.insert(5)
circularDLL2.insert(9)
circularDLL2.insert(2)
circularDLL2.insert(10)
circularDLL2.insert(12)
circularDLL2.traverseCDLL()

print()

# sumList(circularDLL1, circularDLL2)
print(intersection(circularDLL1, circularDLL2))