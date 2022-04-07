# def capitalizeWords(arr):
#     result = []
#     for i in arr:
#         result.append(i.upper())
#     return result

# print(capitalizeWords(['i', 'am', 'learning', 'recursion']))

# def capitalizeWords(arr):
#     res = []
#     if len(arr) == 0:
#         return result
#     else:
#         return res.append((arr[0].upper() + arr[1:])
    
def helper(arrOfStrs, index, result):
    if index >= len(arrOfStrs):
        return result
    result.append(arrOfStrs[index].upper())
    return helper(arrOfStrs, index + 1, result)

def capitalizeWords(arrOfStrs):
    index, result = 0, []
    return helper(arrOfStrs, index, result)

print(capitalizeWords(['i', 'am', 'learning', 'recursion']))