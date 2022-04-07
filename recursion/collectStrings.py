obj = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {
                "info": "bar",
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}


def collectStrings(obj):
    strings = []
    for key in obj:
        if type(obj[key]) is str:
            strings.append(obj[key])
        if type(obj[key]) is dict:
            strings = strings + collectStrings(obj[key])
    return strings


print(collectStrings(obj))