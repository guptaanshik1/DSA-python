"""
Complete the function maxStrength(n)
where n is the id of random player to be selcted at first.
The next id of any other player can be called by the sum of factorial of digits of previous player.
populate a array with the id of different players which forms a team and then find the strength of the team
and strength of team can be calculated by id of the leader multiplied with length of the team.
id of the leader is the maximum id in the team

For example:
i/p: 450
so team = {450, 145}
o/p: 900
"""

"""
Find the number of which has increasing profit in consecutive months based on the analysis parameter
i/p: {1, 2, 3, 3, 4, 5}, analysis parameter = 3
o/p: 2
reason = 3 months have t0 be checked as analysis parameter is 3
so 1, 2, 3 is first then 3, 4, 5 is second
"""


def factOfDigits(n):
    res, d = 0, 0
    while n > 0:
        fact = 1
        d = n % 10
        for i in range(d, 1, -1):
            fact *= i
        res += fact
        n = int(n / 10)
    return res

def maxStrength(n):
    group = []
    nextId = 0
    group.append(n)
    while True:
        nextId = factOfDigits(n)
        if nextId in group:
            break
        group.append(nextId)
        n = nextId
    # return group
    return max(group) * len(group)

print(maxStrength(5))