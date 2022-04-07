def helper(s, index, count):
    vowels = 'aeiouAEIOU'
    if index >= len(s):
        return count
    if s[index] not in vowels:
        count = count + 1

    return helper(s, index + 1, count)

def countConsonants(s):
    index, count = 0, 0
    return helper(s, index, count)

print(countConsonants("Anshik"))