def __helper(p, up):
    if up == "":
        print(p)
        return

    """
    size of positions for a character in next recursive call = size of processed + 1
    the next level will have size of processed + 1 recursive call
    """
    ch = up[0]
    for i in range(len(p) + 1):
        first = p[0:i]
        second = p[i:len(p)]
        __helper(first + ch + second, up[1:])

def permutation(s):
    __helper("", s)

s = "abc"
permutation(s)

def __helperReturn(p, up):
    if up == "":
        ans = []
        ans.append(p)
        return ans

    ch = up[0]
    ans = []

    for i in range(len(p) + 1):
        first = p[0:i]
        second = p[i:len(p)]
        ans.extend(__helperReturn(first + ch + second, up[1:]))

    return ans

def permutationReturn(s):
    return __helperReturn("", s)

s = "abc"
print(permutationReturn(s))

def __helperCount(p, up):
    if up == "":
        return 1

    ch = up[0]
    count = 0

    for i in range(len(p) + 1):
        first = p[0:i]
        second = p[i:len(p)]
        count += __helperCount(first + ch + second, up[1:])
    
    return count

def permutationCount(s):
    return __helperCount("", s)

s = "abc"
print(permutationCount(s))