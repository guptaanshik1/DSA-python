class Queue:
    def __init__(self, maxSize = 0):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top + 1 == self.maxSize and self.start == 0:
            return True
        elif self.top + 1 == self.start:#There is no empty cell between start and top
            return True
        else:
            return False

    def printQueue(self):
        if self.isEmpty() or self.items == None:
            print("There is no element in the queue")
        else:
            for i in self.items:
                print(i, end = " ")

    def enqueue(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0#setting top to first element
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value#insert element where top is pointing
        return "The element has been inserted in the Queue"

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:# only element in the queue
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:#if start is at the last
                self.start = 0
            else:
                self.start += 1
            self.items[self.start] = None#ignore the item to which start is pointing
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1

customQueue = Queue(5)

print(customQueue.isEmpty())
print(customQueue.isFull())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue.isEmpty())
customQueue.enqueue(5)
print(customQueue.isFull())

customQueue.printQueue()
print()
print(customQueue.peek())
print(customQueue.dequeue())
customQueue.printQueue()

customQueue.delete()
customQueue.printQueue()