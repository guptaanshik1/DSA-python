from random import randint

class Node:
    def __init__(self, value = None):
        self.value = None
        self.prev = None
        self.next = None
    
    def printNode(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        if self.head is None:
            return "There is no node in the linked list"
        else:
            node = self.head
            while node:
                print(node.value, end = ' -> ')
                node = node.next

    def printLL(self):
        values = []
        for i in self:
            values.append(str(i.value))
        return ' -> '.join(values)

    def lengthList(self):
        len = 0
        node = self.head
        while node:
            len += 1
            node = node.next
        return len

    def insert(self, value):
        #if the linked list is empty then add node at beginning
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            #if linked list is not empty then add node in the last
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.insert(randint(min_value, max_value))
        return self

customLL = LinkedList()
customLL.generate(10, 1, 99)
print(customLL.traverse())
print(customLL.lengthList())