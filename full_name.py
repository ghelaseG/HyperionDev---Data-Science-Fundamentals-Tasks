# Compulsory Task 1
# "This program will be used to validate that a user inputs at least two names when
#asked to enter their full name."

first_name = input('Please enter your first name:\n').capitalize()
last_name = input('Please enter your surname:\n').capitalize()
full_name = first_name + " " + last_name
print(full_name)

if len(full_name) == 1: #we use 1 because of the space between the names from variable full_name
    print("You haven't entered anything. Please enter your full name.")
elif len(full_name) < 5:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(full_name) > 26:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")