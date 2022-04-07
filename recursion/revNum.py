sm = 0

def reverseNum(n):
    global sm
    if n == 0:
        return

    rem = n % 10
    sm = sm * 10 + rem
    reverseNum(n // 10)
    return sm

print(reverseNum(1234))