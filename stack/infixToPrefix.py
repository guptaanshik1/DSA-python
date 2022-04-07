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

    def rev_expr(self, expr):
        rev = ''
        for i in range(len(expr) - 1, -1, -1):
            if expr[i] == '(':
                rev += ')'
            elif expr[i] == ')':
                rev += '('
            else:
                rev += expr[i]
        return rev

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

    def rev_post_expr(self, postfix_expr):
        return postfix_expr[::-1]

    def infixToPrefix(self, expr):
        """
        1. reverse the expr as: ( -> ) and ) -> (
        2. find the postfix of reversed expr
        3. reverse the resultant postfix expr
        4. return the string as prefix
        """
            
        reversed_expr = self.rev_expr(expr)
        postfix_expr = self.infixToPostfix(reversed_expr)
        return self.rev_post_expr(postfix_expr)

convert = Conversion()

print(convert.infixToPrefix("(2+(3*4)*6)"))