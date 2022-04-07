class Conversion:
    def __init__(self):
        self.stack = []
        self.result = []
        self.precedence = {
            '(': 0,
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    # method to check whether current character has smaller precedence than character at top of stack
    def checkPrecedence(self, ch):
        try:
            if self.stack:
                top = self.precedence[self.stack[-1]]
                curr = self.precedence[ch]

                return True if top >= curr else False

        except KeyError:
            return False

    def infixToPostfix(self, expr):
        for ch in expr:
            if ch.isalnum():
                self.result.append(ch)
            elif ch == '(':
                self.stack.append(ch)
            elif ch == ')':# when ')' then pop till '(' is not encountered in stack
                popped = self.stack.pop()
                while True:
                    if popped == '(': break
                    self.result.append(popped)
                    popped = self.stack.pop()
            else:
                while self.stack and self.checkPrecedence(ch):# keep popping till operator with lower precedence is not found
                    self.result.append(self.stack.pop())
                self.stack.append(ch)
        
        while self.stack:
            self.result.append(self.stack.pop())

        return "".join(self.result)

convert = Conversion()

print(convert.infixToPostfix("(2*3+4*(5-6))"))