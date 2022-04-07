def removeAdjacent(s):
    if len(s) == 0:
        return ''
    ch = s[0]
    string = removeAdjacent(s[1:])
    if ch == string[0]:
        return string
    else:
        return ch + string

print(removeAdjacent('AABBBCDDD'))