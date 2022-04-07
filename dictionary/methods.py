myDict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}

#copy()
newDict = myDict.copy()
print(myDict)
print(newDict)

#fromkeys()
secDict = {}.fromkeys([1, 2, 3], 4)
print(secDict)

#get()
# print(myDict.get('one', 1)) value is optional
print(myDict.get('one'))

#items()
print(myDict.items())

#key()
print(myDict.keys())

#setdefault()
print(myDict.setdefault('five', 5))
print(myDict.setdefault('six'))
print(myDict)

#values()
print(myDict.values())

#update()
new2Dict = {'a': 'A', 'b': 'B'}

myDict.update(new2Dict)
print(myDict)

#in
print('a' in myDict)

#all()
boolDict1 = {
    1: True,
    2: True
}
print(all(boolDict1))

#any()
boolDict2 = {
    1: False,
    2: True
}

print(any(boolDict2))

#len()
print(len(myDict))

#sorted()
vowelDict = {
    'eas': 2,
    'as': 1,
    'uq': 5,
    'iddad': 3,
    'oqwqw': 4
}

print(vowelDict)
print(vowelDict)
print(sorted(vowelDict))
print(sorted(vowelDict, reverse = True))
print(sorted(vowelDict, reverse = False, key = len))

