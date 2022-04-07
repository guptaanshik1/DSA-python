# from random import randint

def findMissing(li, n):
    n = len(li) + 1
    sum1 = (n * (n + 1)) / 2
    # sum1 = (20 * 21) / 2
    sum2 =  sum(li)
    print(sum1 - sum2)

li = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
findMissing(li, 100)

#generate a list of random numbers 1 to 100 and no numbers should repeat