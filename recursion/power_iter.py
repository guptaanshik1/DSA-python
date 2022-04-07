base = int(input("Enter base\n"))
exp = int(input("Enter exponent\n"))
res = 1

if exp == 0:
    res = 1
elif exp == 1:
    res = base
else:
    for i in range(1, exp + 1):
        res = res * base

print(res)