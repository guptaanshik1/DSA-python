def helper(s, index, res):
    if index >= len(s):
        return res
    if s[index] == "p" and s[index + 1] == "i":
        res = res + "3.14"
        return helper(s, index + 2, res)    
    res = res + s[index]
    return helper(s, index + 1, res)

def replacePI(s):
    index, res = 0, ''
    return helper(s, index, res)

print(replacePI("pippxxppiixipi"))

print(replacePI("pippppiiiipi"))