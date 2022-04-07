sm = 0

def rev(n):
    global sm
    if n == 0:
        return

    rem = n % 10
    sm = sm * 10 + rem
    rev(n // 10)

    return sm

def ispalin(n):
    return n == rev(n)

n = 1001
print(ispalin(n))