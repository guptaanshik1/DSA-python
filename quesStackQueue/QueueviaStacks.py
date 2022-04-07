class Stack:
    def __init__(self):
        self.list = []

    def printStack(self):
        if len(self.list) == 0:
            print("There is no element in the stack")
        else:
            for i in self.list:
                print(i, end = " ")

    def lengthList(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()

class QueueviaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def printQueue(self):
        if self.inStack.printStack():
            print(i, end = " ")

    def enqueue(self, item):
        self.inStack.push(item)
        
    def dequeue(self):
        while self.inStack.lengthList():
            popStack = self.inStack.pop()
            self.outStack.push(popStack)
        toBeReturned = self.outStack.pop()
        while self.outStack.lengthList():
            popStack = self.outStack.pop()
            self.inStack.push(popStack)
        return toBeReturned

customQueue = QueueviaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
customQueue.printQueue()

print()

print(customQueue.dequeue())
customQueue.printQueue()
