class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def traverseStack(self):
        if self.list == None:
            print("There is no element in the stack to traverse")
        else:
            for i in range(len(self.list) - 1, -1, -1):
                print(self.list[i])

    def push(self, value):
        self.list.append(value)
        return "The element has been inserted into the stack"

    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack to pop"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack to pop"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)

customStack.traverseStack()
# print(customStack.pop())

# print()
# customStack.traverseStack()
print()
print(customStack.peek())

print()
customStack.delete()
customStack.traverseStack()