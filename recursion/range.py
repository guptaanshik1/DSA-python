def range(num):
    assert num >= 0 and int(num) == num, "The number should be positive and an integer only"
    if num == 1:
        return num
    else:
        return num + range(num - 1)

print(range(6))

print(range(10))