class Evaluate:
    def __init__(self):
        self.stack = []

    def evaluatePostfix(self, expr):
        for ch in expr:
            if ch not in '+-/*^%':
                self.stack.append(ch)
            else:
                a = self.stack.pop()
                b = self.stack.pop()

                result = int(eval(b + ch + a))
                self.stack.append(str(result))

        return int(self.stack.pop())

evaluate = Evaluate()

print(evaluate.evaluatePostfix("234*6*+"))

print(evaluate.evaluatePostfix(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))