class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def createNode(self, nodeValue):
        firstNode = Node(nodeValue)
        self.head = firstNode
        self.tail = firstNode
        firstNode.next = None
        print("The node has been created successfully")

    def traverseSLL(self):
        if self.head is None:
            print("There is no node in the single linked list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("There is no node in the single linked list")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
                newNode.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                tempNode.next = newNode

    def searchSLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the single linked list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does exist in the single linked list"

    def deleteNode(self, location):
        if self.head is None:
            print("There is no node in the single linked list")
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
                    while tempNode:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = tempNode.next.next

    def deleteEntireSLL(self):
        if self.head is None:
            print("There is no node in the single linked list")
        else:
            self.head = None
            self.tail = None

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

    def removeDups(self):
        if self.head is None:
            print("There is no node in the single linked list")
        else:
            tempNode = self.head
            while tempNode:
                runner = tempNode
                while runner:
                    # print("Runner:", runner.value)
                    # print("Tempnode", tempNode.value)
                    if runner.next.value == tempNode.value:
                        runner.next = tempNode.next.next
                    else:
                        runner = runner.next
                tempNode = tempNode.next
        return self.traverseSLL()

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

    # def partition(self, value):
    #     tempNode = self.head
    #     self.head = self.tail
    #     while tempNode:
    #         nextNode = tempNode.next
    #         tempNode.next = None
    #         if tempNode.value < value:
    #             tempNode.next = self.head
    #             self.head = tempNode
    #         else:
    #             self.tail.next = tempNode
    #             self.tail = tempNode
    #         tempNode = nextNode
    #     if self.tail is not None:
    #         self.tail.next = None

    def partition(self, partitionValue):
        tempNode = self.head
        while tempNode:
            if tempNode.value > partitionValue:
                tempNode.next = self.head
                self.head = tempNode
                tempNode = tempNode.next
            else:
                self.tail.next = tempNode
                self.tail = tempNode
                tempNode.next = None
                tempNode = tempNode.next
            # if self.tail.next == None:
            #     break
        if self.tail.next == None:
            self.tail.next = None

    def insert(self, nodeValue):
        newNode = Node(nodeValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

def sumList(ll1, ll2):
    tempLL1 = ll1.head
    tempLL2 = ll2.head
    carry = 0
    ll = SingleLinkedList()
    while tempLL1 or tempLL2:
        result = carry
        if tempLL1:
            result += tempLL1.value
            tempLL1 = tempLL1.next
        if tempLL2:
            result += tempLL2.value
            tempLL2 = tempLL2.next
        ll.insert(int(result % 10))#1's digit
        carry = result / 10#10's digit
    ll.traverseSLL()

def intersection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        print("false")

    len1 = ll1.lengthList()
    len2 = ll2.lengthList()
    print()
    print(len1)
    print()
    print(len2)

    shorter = ll1 if len1 < len2 else ll2#shorter is ll1 if len1 is shorter
    longer = ll2 if len1 < len2 else ll1#longer is ll2 if len1 is shorter
    print()
    shorter.traverseSLL()
    print()
    longer.traverseSLL()
    print()

    extraNode = longer.lengthList() - shorter.lengthList()
    print(extraNode)

    shorterNode = shorter.head
    longerNode = longer.head

    for i in range(extraNode):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        if shorterNode.value == longerNode.value:
            break
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode.value

singleLL = SingleLinkedList()
singleLL1 = SingleLinkedList()
singleLL2 = SingleLinkedList()

singleLL.createNode(1)
singleLL.insertNode(0, 0)
singleLL.insertNode(2, -1)
singleLL.insertNode(3, -1)
singleLL.insertNode(10, 1)
singleLL.insertNode(20, 3)

# singleLL.traverseSLL()

print()

# print(singleLL.searchSLL(2))
# print(singleLL.searchSLL(10))

# singleLL.deleteNode(2)

# singleLL.deleteEntireSLL()

# singleLL.removeDups()
print()
# singleLL.traverseSLL()
# print(singleLL.nthToLast(4))
# print(singleLL.partition(8))

singleLL1.createNode(2)
singleLL1.insertNode(4, -1)
singleLL1.insertNode(3, -1)
# singleLL1.insertNode(8, -1)
# singleLL1.insertNode(10, -1)
# singleLL1.insertNode(12, 1)

singleLL2.createNode(5)
singleLL2.insertNode(6, -1)
singleLL2.insertNode(4, -1)
# singleLL2.insertNode(8, -1)
# singleLL2.insertNode(10, -1)

singleLL1.traverseSLL()
print()
singleLL2.traverseSLL()
print()
print(sumList(singleLL1, singleLL2))

# sumList(singleLL1, singleLL2)
# print()

# print(intersection(singleLL1, singleLL2))

# print()

# singleLL.traverseSLL()

# print()

# singleLL.partition(4)

# singleLL.traverseSLL()