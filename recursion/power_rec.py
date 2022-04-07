def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "The exponent should be positive and an integer"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp - 1)

print(power(-2, 2))