def helper(s, index, ans):
    if index >= len(s):
        return ans
    if s[index].isupper():
        ans = s[index]
        return ans
    return helper(s, index + 1, ans)

def findUppercase(s):
    index, ans = 0, ''
    return helper(s, index, ans)

print(findUppercase("anshIk"))