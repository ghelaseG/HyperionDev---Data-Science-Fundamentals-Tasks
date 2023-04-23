# create a program that determines the award a person competing in a triathlon will receive.

# we ask the user to insert the times(in minutes) for all three events of a triathlon
swimming = int(input('Please enter the time(in minutes) taken to complete the swimming event: '))
cycling = int(input('Please enter the time(in minutes) taken to complete the cycling event:  '))
running = int(input('Please enter the time(in minutes) taken to complete the running event:  '))

# we now store them in a tuple and print the total output
total_triathlon = (swimming,cycling,running) 
print(f"\nYou're total time to complete the triathlon is: {sum(total_triathlon)}.")

# following if statements will display the award a participant receives by using comparison and logical operators

# total time within qualifying time (100)
if sum(total_triathlon) <= 100:
    print("\nCongratulations! You've been awarded \"Provincial Colors\".")

# within 5 minutes of qualifying time
elif sum(total_triathlon) > 100 and sum(total_triathlon) <= 105:
    print("\nCongratulations! You've been awarded \"Provincial Half Colors\".")

# within 10 minutes of qualifying time
elif sum(total_triathlon) > 105 and sum(total_triathlon) <= 110:
    print("\nCongratulations! You've been awarded \"Provincial Scroll\".")

# more than 10 minutes of qualifying time
else:
    print("\nWe're sorry, you will not receive a reward.")
