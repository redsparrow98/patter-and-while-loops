#============== Final Code ================

# use a global variable that you can update in the loop
inputs = []

# Have a initial variable that controls the while loop
user_input = int(input("Please enter a number (-1 to exit): "))

# have a while loop with a condition that needs to be met to exit
while user_input != -1:
    # if the condition is not met add up
    # the user input to the global variable
    inputs.append(user_input)

    # if the condition isn't met keep asking for input
    user_input = int(input("Please enter a number (-1 to exit): "))



# After we have all the inputs it calculates the sum of the inputs
# excluding -1
# and calculate the average of the total inputs and print it
total = sum(inputs)
average = total / len(inputs)
print(average)
