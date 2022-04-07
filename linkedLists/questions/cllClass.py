class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createNode(self, nodeValue):
        firstNode = Node(nodeValue)
        firstNode.next = firstNode
        self.head = firstNode
        self.tail = firstNode
        print("The node has been created successfully")

    def traverseCLL(self):
        if self.head is None:
            print("There is no node in the circular linked list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("There is no node in the circular linked list")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
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
                newNode.next = tempNode.next
                tempNode.next = newNode

    def searchCLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the circular linked list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail.next:
                    break
                tempNode = tempNode.value
            return "The node does not exist in the circular linked list"

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
                    while tempNode:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next

    def deleteEntireCLL(self):
        if self.head is None:
            print("There is no node in the circular linked list")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None

    def insert(self, nodeValue):
        newNode = Node(nodeValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            # self.tail.next = newNode
            # self.tail = self.tail.next
            # newNode.next = self.head
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode

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
    ll = CircularLinkedList()
    while tempLL1 or tempLL2:
        result = carry
        if tempLL1:
            result += tempLL1.value
            print("1:", tempLL1.value, end = "\n")
            tempLL1 = tempLL1.next

        if tempLL2:
            result += tempLL2.value
            print("2:", tempLL2.value, end = "\n")
            tempLL2 = tempLL2.next

        ll.insert(int(result % 10))#1's digit
        carry = result / 10#10's digit
        if tempLL2 == ll2.tail.next:
            break
    return ll.traverseCLL()

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
    shorter.traverseCLL()
    print()
    longer.traverseCLL()
    print()

    extraNode = longer.lengthList() - shorter.lengthList()
    print(extraNode)

    shorterNode = shorter.head
    longerNode = longer.head

    for i in range(extraNode):
        longerNode = longerNode.next
        if longerNode == longer.tail.next:
            break

    while shorterNode is not longerNode:
        if shorterNode.value == longerNode.value:
            break
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode.value



circularLL = CircularLinkedList()
circularLL.createNode(1)
circularLL.insertNode(0, 0)
circularLL.insertNode(2, 0)
circularLL.insertNode(3, -1)
circularLL.insertNode(4, -1)
circularLL.insertNode(10, 1)
circularLL.insertNode(20, 3)

# circularLL.traverseCLL()

print()

# circularLL.deleteNode(2)

# print(circularLL.nthToLast(4))

circularLL1 = CircularLinkedList()
circularLL2 = CircularLinkedList()

circularLL1.createNode(6)
circularLL1.insertNode(1, 0)
circularLL1.insertNode(7, 0)
# circularLL1.insertNode(8, -1)
# circularLL1.insertNode(10, -1)
# circularLL1.insertNode(12, 1)
circularLL1.traverseCLL()

print()

circularLL2.createNode(2)
circularLL2.insertNode(9, 0)
circularLL2.insertNode(5, 0)
# circularLL2.insertNode(8, -1)
# circularLL2.insertNode(10, -1)
circularLL2.traverseCLL()

print()


sumList(circularLL1, circularLL2)

# print(intersection(circularLL1, circularLL2))