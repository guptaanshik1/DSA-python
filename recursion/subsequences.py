def __helper(s, index, output):
    if index >= len(s):
        print(output)
        return
    
    __helper(s, index + 1, output)
    __helper(s, index + 1, output + s[index])

def subsequences(s):
    return __helper(s, 0, "")

subsequences("abc")

def __helper2(p, up):
    if up == "":# whenever unprocesses string is empty then print processed string
        print(p)

        return

    ch = up[0]

    __helper2(p, up[1:])
    __helper2(p + ch, up[1:])

def subseq(s):
    return __helper2("", s)

print()
subseq("abc")

def __helperAscii(p, up):
    if up == "":
        print(p)
        return

    ch = up[0]
    __helperAscii(p, up[1:])
    __helperAscii(p + ch, up[1:])
    __helperAscii(p + str(ord(ch)), up[1:])

def subseqAscii(s):
    return __helperAscii("", s)

print()
subseqAscii("ab")

# returning subsequences in a list

def __helperRet(p, up):
    if up == "":
        ans = []
        ans.append(p)
        return ans
    
    ch = up[0]
    left = __helperRet(p + ch, up[1:])# left is array returned from left call
    right = __helperRet(p, up[1:])# right is array returned from right call
    left.extend(right)
    return left

def subseqReturn(s):
    return __helperRet("", s)

s = "abc"
print()
print(subseqReturn("abc"))

def __helperAsciiRet(p, up):
    if up == "":
        ans = []
        ans.append(p)
        return ans

    ch = up[0]
    firstCall = __helperAsciiRet(p + ch, up[1:])
    secondCall = __helperAsciiRet(p + str(ord(ch)), up[1:])
    thirdCall = __helperAsciiRet(p, up[1:])
    firstCall.extend(secondCall)
    firstCall.extend(thirdCall)
    return firstCall

def subseqReturnAscii(s):
    return __helperAsciiRet("", s)

print()
print(subseqReturnAscii("ab"))