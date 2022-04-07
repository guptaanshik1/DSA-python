# def exp(n):
#     if n == 0:
#         return 1
#     ans = exp(n // 2)
#     if (n & 1):
#         return 2 * ans * ans
#     else:
#         return ans * ans

# def power(base, raised):
#     if raised == 0:
#         return 1
#     ans = power(base, raised // 2)
#     if (raised & 1):
#         return base * ans * ans
#     else:
#         return ans * ans

def function(base, exp):
    exp = abs(exp)
    if exp == 0:
        return 1
    res = function(base, exp // 2)
    if exp & 1:
        return base * res * res
    else:
        return res * res
        
def myPow(x, n):# in case of negative power
    if n < 0:
        return 1 / float(function(x, n))
    else:
        return function(x, n)
        
# print(exp(10))
# print(power(3, 5))

print(myPow(4, 3))