#=======================  Code  ============================

# set a variable for the string that
# we want to print theater with
STAR = "*"

# set another variable that we can update with every iteration
# for the else statement
num = 5

# do a for loop for range of 10

for i in range (10):
    # if the i is less or equal to 5 the we print the * the amount of times
    # that the i is equal to at the certain iteration
    if i < 5:
        print(STAR * (i + 1))

    # Else if the i is bigger of equal to 6 then we deduct 1 from the n variable
    # and print out as many * timed by the n variable
    elif i >= 6:
        num -= 1
        print(STAR * num)
