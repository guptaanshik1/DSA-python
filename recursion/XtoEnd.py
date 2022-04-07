def helper(s, index, res, X):
    if index >= len(s):
        return res + X
    if s[index] == 'x':
        X = X + s[index]
    else:
        res = res + s[index]

    return helper(s, index + 1, res, X)

def moveXToEnd(s):
    index, res, X = 0, '', ''
    return helper(s, index, res, X)

def anotherMethod(s):
    if len(s) == 0:
        return ''
    ch = s[0]
    string = anotherMethod(s[1:])
    
    if ch == 'x':
        return string + ch
    else:
        return ch + string

print(moveXToEnd("axxbdxcefxhix"))

print(anotherMethod("axxbdxcefxhix"))