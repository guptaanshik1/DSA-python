def helper(arr, index, output):
    if index >= len(arr):
        for i in output:
            print(i, end = ' ')
        print()
        return
    
    helper(arr, index + 1, output)
    output.append(arr[index])
    helper(arr, index + 1, output)

arr = [1, 2, 3]
output = []
helper(arr, 0, output)