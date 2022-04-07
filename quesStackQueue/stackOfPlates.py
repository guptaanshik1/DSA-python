class PlateOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def printStack(self):
        if len(self.stacks) == 0:
            print("There is no element in the stack")
        else:
            for i in self.stacks:
                print(i, end = " ")

    def lengthStack(self):
        return len(self.stacks)

    def push(self, item):
        if self.stacks.lengthStack() > 0 and self.stacks[-1].lengthStack() < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append(item)

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            return self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None

customStack = PlateOfStacks(2)
customStack.push(1)
customStack.push(2)
customStack.printStack()