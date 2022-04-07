count = 0

def countZeros(n):
    global count

    if n == 0:
        return
    rem = n % 10
    if rem == 0:
        count += 1
    countZeros(n // 10)
    return count

def helper(n, cnt):
    if n == 0:
        return cnt
    rem = n % 10
    if rem == 0:
        return helper(n // 10, cnt + 1)
    return helper(n // 10, cnt)

def countZeros2(n):
    return helper(n, 0)

print(countZeros(30204))
print(countZeros2(30204))