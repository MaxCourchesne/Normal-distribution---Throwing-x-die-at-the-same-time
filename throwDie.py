import random
import matplotlib.pyplot as plt


numberofdice = ""
while not isinstance(numberofdice, int):
    try:
        numberofdice = int(input("How many dice? : "))
    except ValueError:
        print("the answer must be a number")


numberofrolls = 100000

results = {}
def rolls(num):
    for roll in range(num):
        sum = 0
        for x in range(numberofdice):
            dice = random.choice([1, 2, 3, 4, 5 , 6])
            sum += dice
        if sum in results:
            results[sum] += 1
        else:
            results[sum] = 0

rolls(numberofrolls)


sums = [x[0] for x in results.items()]
times = [x[1] for x in results.items()]
'''print(results)
print(sums)
print(times)
'''
# setting the x axis values
if numberofdice < 16:
    plt.xticks([x for x in range(0, 1000)])
elif numberofdice < 31:
    plt.xticks([x for x in range(0, 1000) if x%2 == 0])
else:
    plt.xticks([x for x in range(0, 1000) if x%4 == 0])


plt.title(f"how many times a certain number was obtained throwing {numberofdice} dice at a time {numberofrolls} times")
plt.bar(sums, times)
plt.show()