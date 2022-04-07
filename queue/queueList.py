class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == []:
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
        self.items.append(value)
        return "The element has been inserted in the queue"

    def dequeue(self):
        if self.isEmpty() or self.items == None:
            return "The stack is empty"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty() or self.items == None:
            return "The stack is empty"
        else:
            return self.items[0]

    def delete(self):
        self.items = None

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue.isEmpty())
customQueue.printQueue()

print()
print(customQueue.dequeue())
customQueue.printQueue()
print()

customQueue.delete()
customQueue.printQueue()

print(customQueue.peek())