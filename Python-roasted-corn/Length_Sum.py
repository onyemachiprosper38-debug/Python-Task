import random

count = 0
number_list = []

for numbers in range(10):
    number = random.randint(1, 50)
    number_list.append(number)
    count += 1
print(number_list)

 
 
print("The length of list is", count)


sum_of_number = sum(number_list)
print("Sum =", sum_of_number)

 
multiply = 1
for num in range(len(number_list)):
    multiply *= num

print("Multiplication =", multiply)

 
average = sum(number_list) / len(number_list)
print("Average =", round(average, 3))
