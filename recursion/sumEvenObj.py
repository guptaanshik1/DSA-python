obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 4,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}


def evenSum(obj):
  sm = 0
  for key in obj:
    if type(obj[key]) is int:
      if obj[key] % 2 == 0:
        sm += obj[key]
    if type(obj[key]) is dict:
      sm += evenSum(obj[key])
  return sm

print(evenSum(obj1))
