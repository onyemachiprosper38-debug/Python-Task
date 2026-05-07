#the simple problem in number 4.3 in chapter 4 is that they didn't add return statement.


def cube(x):
   return x ** 3

print('the cube of 2 is ', cube(2))


#what the code in number 4.4 in chapter4 does. it add up all the square of value inside x 


def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y
print('the mystery of [1, 2, 3] is: ', mystery([1, 2, 3]))


def second_since_midnight(hour, minute, second):
    hour_in_seconds = hour * 3600
    minute_in_seconds = minute * 60
    total_seconds = hour_in_seconds + minute_in_seconds + second
    return total_seconds
    print(total_seconds)
