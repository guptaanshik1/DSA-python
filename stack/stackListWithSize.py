class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
            
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def traverseStack(self):
        if self.list == None or self.isEmpty():
            print("There is no element in the stack")
        else:
            for i in range(len(self.list) - 1, -1, -1):
                print(self.list[i])

    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been added to the stack"

    def pop(self):
        if self.isEmpty() or self.list == None:
            return "There is no element in the stack to pop"
        else:
            self.list.pop()

    def peek(self):
        if self.isEmpty() or self.list == None:
            return "There is no element in the stack"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None

customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())

customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(1)

print(customStack.push(5))

customStack.traverseStack()
print()
print(customStack.peek())

customStack.delete()
customStack.traverseStack()