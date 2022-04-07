#searching method
def searchDict(d, value):
    for key in d:
        if d[key] == value:
            return key, value
        else:
            return "The value does not exist"

myDict = {
    'name': 'Anshik',
    'language': 'Python',
}

print(myDict)

#inserting
myDict['course'] = 'DSA'
print(myDict)

#updating
myDict['language'] = 'JavaScript'
print(myDict)

#traverse
for key in myDict:
    print(key, ": ", myDict[key])

#calling the searching method
print(searchDict(myDict, 'Anshik'))

#deleting

# print(myDict.pop('course'))
# print(myDict)

print(myDict.popitem())
print(myDict)

# myDict.clear()
# print(myDict)

del myDict['language']
print(myDict)

# del myDict - to delete the entire dictionary
