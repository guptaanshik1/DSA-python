def helper(s, index, output):
    keypad = [
        "",
        "./",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
    ]

    if index >= len(s):
        print(output)
        return
    
    ch = s[index]
    key = keypad[int(ch)]
    # print(key)
    for i in range(len(key)):
        helper(s, index + 1, output + key[i])

def printDigits(s):
    index, output = 0, ""
    return helper(s, index, output)

s = "23"
printDigits(s)