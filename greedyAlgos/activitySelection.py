def activitySelect(activities):
    activities.sort(key = lambda x: x[2])#sorting activities on 2nd index
    i = 0
    fisrtA = activities[i][0]
    print(fisrtA)
    #looping through the sorted activities
    for j in range(len(activities)):#i is previous activity ad j is next activity
        # print(activities[j][0])
        # checking whether the finish time of previous activity is equal or greater than the next activity
        # print(activities[j][1], activities[i][2])#[i][2] is finish time and [j][1] is start time
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j

def sortFinishTime(activities):
    for i in range(len(activities)):
        for j in range(i + 1, len(activities)):
            if activities[i][2] > activities[j][2]:
                swap = activities[i]
                activities[i] = activities[j]
                activities[j] = swap
    return activities

def activitySelection(activities):
    sortFinishTime(activities)
    i = 0
    firstAct = activities[i][0]
    print(firstAct)
    for j in range(len(activities)):
        #start time of activity2 is 3 and end time of activity1 is 2(example)
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j








activities = [
    ["A1", 0, 6],
    ["A2", 3, 4],
    ["A3", 1, 2],
    ["A4", 5, 8],
    ["A5", 5, 7],
    ["A6", 7, 8]
]
print(activities)
# sortFinishTime(activities)
# print()
# print(activities)
activitySelect(activities)
activitySelection(activities)