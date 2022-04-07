def sumOfDigits(n):
    assert n >=0 and int(n) == n, "The number shoule be greater than 0 and an integer"
    if n in [0, 9]:
        return n
    else:
        return int(n % 10) + sumOfDigits(int(n / 10))

print(sumOfDigits(22))