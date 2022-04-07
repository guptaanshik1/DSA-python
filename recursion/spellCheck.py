def spellCheck(num):
    words = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]

    if num == 0:
        return
    
    spellCheck(num // 10)
    number = num % 10
    print(words[number], end=' ')

spellCheck(1199)