def sumOfDigits(num):
    sum = 0
    temp = num
    while(num != 0):
        sum = sum + (num % 10)
        num = num // 10
    return sum

n = int(input("Enter a positive integer\n"))
print(sumOfDigits(n))