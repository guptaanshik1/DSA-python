# def capitalizeFirst(arr):
#     result = []
#     for i in arr:
#         result.append(i[0].upper() + i[1:])
#     return result
    
# print(capitalizeFirst(['car', 'taco', 'banana']))

# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

def helper(arrOfStrs, index, result):
    if index >= len(arrOfStrs):
        return result

    arrOfStrs[index] = arrOfStrs[index][0].replace(arrOfStrs[index][0], arrOfStrs[index][0].upper()) + arrOfStrs[index][1:]
    result.append(arrOfStrs[index])
    return helper(arrOfStrs, index + 1, result)

def capitalizeFirst(arrOfStrs):
    index, result = 0, []
    return helper(arrOfStrs, index, result)
    
print(capitalizeFirst(['car', 'taco', 'banana']))
# s = ['python', 'list']
# res = []