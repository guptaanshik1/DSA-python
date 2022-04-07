class Evaluate:
    def __init__(self):
        self.stack = []

    def evaluatePrefix(self, expr):
        for i in range(len(expr) - 1, -1, -1):
            if expr[i].isdigit():
                self.stack.append(expr[i])
            else:
                a = self.stack.pop()
                b = self.stack.pop()

                result = eval(a + expr[i] + b)
                self.stack.append(str(result))
        
        return int(self.stack.pop())
        
evaluate = Evaluate()

print(evaluate.evaluatePrefix("+2**346"))