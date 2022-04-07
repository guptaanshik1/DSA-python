def helper(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return helper(s, left + 1, right - 1)

def isPalin(s):
    left, right = 0, len(s) - 1
    return helper(s, left, right)

print(isPalin('tacocat'))

print(isPalin('foobar'))