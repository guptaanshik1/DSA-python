def reverseString(strng):
    if len(strng) == 0:
        return strng
    else:
        # calling the string after 1 and returning the first element
        return reverseString(strng[1:]) + strng[0]

def helper(s, index, res):
    if index < 0:
        return res
    res = res + s[index]
    return helper(s, index - 1, res)

def reverse(s):
    index, res = len(s) - 1, ''
    return helper(s, index, res)

print(reverseString("python"))

print(reverse('pyhton'))