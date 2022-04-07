def helper(s, index, output):
    if index >= len(s):
        print(output)
        return

    helper(s, index + 1, output)
    helper(s, index + 1, output + s[index])
    helper(s, index + 1, output + str(ord(s[index])))

def substringsWithASCII(s):
    index, output = 0, ''
    return helper(s, index, output)

substringsWithASCII('AB')