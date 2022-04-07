class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

class Stack:
    def __init__(self):
        self.head = None
        #creating stack with head which contains None

    # def stackHead(self, )

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def traverseStack(self):
        if self.LinkedList.head is None:
            print("There is no element in the stack")
        else:
            tempNode = self.LinkedList.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def push(self, nodeValue):
        node = Node(nodeValue)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        return "The element has been inserted in the stack"

    def pop(self):
        if self.isEmpty() or self.LinkedList.head is None:
            return "There is no element in the stack to pop"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty() or self.LinkedList.head is None:
            return "There is no element in the stack"
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None

def createStackHead(stack, nodeValue):
    newNode = Node(nodeValue)
    head = newNode
    return head

def traverseStack(head):
    if head is None:
        print("There is no element in the stack")
    else:
        tempNode = head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next


customStack = Stack()
headStack = createStackHead(customStack, 1)
pushRec(headStack, 2)
pushRec(headStack, 3)
pushRec(headStack, 4)
traverseStack(headStack)
# print(customStack.isEmpty())
# customStack.pushRec(1)
# customStack.pushRec(2)

# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# customStack.push(4)

# customStack.traverseStack()
# print()

# print(customStack.pop())
# print(customStack.pop())
# print()
# customStack.traverseStack()
# print()
# print(customStack.peek())
# print()
# customStack.delete()
# customStack.traverseStack()