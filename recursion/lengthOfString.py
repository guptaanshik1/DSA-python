def helper(s, index, count):
    if index >= len(s):
        return count
    count = count + 1

    return helper(s, index + 1, count)

def length(s):
    index, count = 0, 0
    return helper(s, index, count)

# def length2(s):
#     if len(s) == 0:
#         return
#     return 1 + len(length2(s[1:]))

print(length("Anshik"))
# print(length2("Anshik"))