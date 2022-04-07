# def averageTemp(temp):
#     temp = []
#     return sum(temp) / len(temp)

temperatures = []
days = int(input("How many days temperature: "))
for i in range(0, days):
    temp_day = int(input("Enter the temperature of day: "))
    temperatures.append(temp_day)

max_temp = max(temperatures)
# print(sum(temperatures), len(temperatures))
print(temperatures)
avg_temp = sum(temperatures) / (len(temperatures))
countDays = 0
for i in range(len(temperatures)):
    if (temperatures[i] > avg_temp):
        countDays += 1

print("The average of temperatures is: ", avg_temp)
print("the number of day(s) temperature was more than the average temperature is: ", countDays)