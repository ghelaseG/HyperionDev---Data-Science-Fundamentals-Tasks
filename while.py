# Write a program that always asks the user to enter a number

total_average = () # create a tuple to store the inputs, excluding -1

while True:
    # The while loop calculate the average of the numbers entered, excluding the -1

    ask_user = float(input("Please enter a number, if you want to exit please enter \"-1\":\n"))
    
    if ask_user != -1:
        total_average = total_average + (ask_user,) #store every number in the tuple

    else:
        total_average = sum(total_average) / len(total_average) #calculate average dividing the total of numbers with how many numbers were entered
        print(f"The average of the numbers entered is {total_average}.")
        break