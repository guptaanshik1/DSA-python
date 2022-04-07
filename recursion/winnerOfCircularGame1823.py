# def helper(arr, index, k):
#     if len(arr) == 1:
#         return arr[0]
#     # print(index)
#     arr.remove(index + k)
#     index = (index + k - 1) % len(arr)
#     return helper(arr, index, k)
#     # print(arr)
#     # print(index)
#     # print(k)

# def josephus(n, k):
#     arr = []
#     for i in range(1, n + 1):
#         arr.append(i)
#     index = 0
#     # print(arr)
#     return helper(arr, index, k)

# print(josephus(5, 2))

def findTheWinner(n, k):
    if n == 1:
        return 1

    return (findTheWinner(n - 1, k) + k - 1) % n + 1

print(findTheWinner(5, 2))