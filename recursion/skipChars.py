def __helperA(s, chIdx, ans):
    if chIdx >= len(s):
        return ans
    
    if s[chIdx] == 'a':
        return __helperA(s, chIdx + 1, ans)
    else:
        ans += s[chIdx]
        return __helperA(s, chIdx + 1, ans)
    return ans

def skipA(s):
    return __helperA(s, 0, "")

s = "baccad"
print(skipA(s))

def skipA2(s):
    if s == "": return ""

    ch = s[0]

    if ch == 'a': return skipA2(s[1:])
    else: return ch + skipA2(s[1:])

print(skipA2("baccad"))

def skipApple(s):
    if s == "": return ""# at the end string will be empty so return empty string

    if s.startswith("apple"):
        return skipApple(s[5:])
    else:
        return s[0] + skipApple(s[1:])

print(skipApple("bcdapplefg"))