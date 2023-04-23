#  Create a loop that will produce the following output:
""" *
    **
    ***
    ****
    ***** """


# create an empty string
star = " " 

# we iterate through the for loop 5 times (5*)
for i in range(5): 
    # we add 1 star at a time
    star += "*"
    print(star)