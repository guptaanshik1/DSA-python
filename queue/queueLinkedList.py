class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def printQueue(self):
        if self.linkedList.head is None:
            print("There is no element in the queue")
        else:
            tempNode = self.linkedList.head
            while tempNode:
                print(tempNode.value, end = " ")
                tempNode = tempNode.next

    def enqueue(self, value):
        node = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.head = None
                self.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode.value

    def peek(self):
        if self.linkedList.head is None:
            return "There is no element in the queue"
        else:
            return self.linkedList.head.value

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
        
customQueue.printQueue()
print()
print(customQueue.peek())
print(customQueue.dequeue())
customQueue.printQueue()
print()
customQueue.delete()

customQueue.printQueue()