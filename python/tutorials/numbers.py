# Getting the largest value and reseting it to a varialbe

numbers = [10,20,30,40,50,60,70,80,1000]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)