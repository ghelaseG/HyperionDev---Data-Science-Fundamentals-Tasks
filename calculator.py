"""Create a simple calculator application that asks a user to enter two
numbers and the operation  (e.g. +, -, x, etc.) using defensive programming"""


# we store every operator that the user can choose with the name into a long string

operators = ("""
Operator	Name	        
+	        Addition	    	
-	        Subtraction	    	
*	        Multiplication		
/	        Division	    	
%	        Modulus	        	
**	        Exponentiation		
//	        Floor division	""")

# we use while loop, as we don't know how many times the user will try to enter the correct input

while True:

    try:
        # let's first ask the user for the input
        first = float(input('Please enter the first number: '))
        second = float(input('Please enter the second number: '))
        print(operators + '\n')
        operator = input('Please enter one of the operator from above: ')

    #we raise errors in case of wrong output    
    except (ValueError, NameError):
        print('Please enter a valid number.')
        continue

    while True:
        # in the following we create if statements with the total of each operator chosen by the user and we raise error if none of them were correctly typed in
        if operator == '+':
            total = first + second
        elif operator == '-':
            total = first - second
        elif operator == '*':
            total = first * second
        elif operator == '/':
            total = first / second
        elif operator == '**':
            total = first ** second
        elif operator == '%':
            total = first % second
        elif operator == '//':
            total = first // second
        else:
            operator = input('Please enter one of the operator from above: ')
            continue
        
        # we show the result rounded to two decimals
        show_result = f'{first} {operator} {second} = {round(total, 2)}'
        print(show_result)
        
        # we use 'a'(append) because the function will either create the file or append to it
        file = open('gg.txt', 'a') 
        file.write(show_result + '\n')
        file.close()    
        break
    
    #ask user to choose what to do next, either to print the text file or to carry on with the calculator
    choice = input('Please choose if you would like to try another equation or see all the text file. \n If you want to see the equations please type in the text file, eg: gg.txt \n Or if you like to try another equation please type (y/n)')
    if choice == 'gg.txt':
        file = open("gg.txt", "r")
        print(file.read())
        break
    if choice.lower() == 'y':
        continue
    elif choice.lower() =='n':
        break
    else:
        print('Try again, answer only with "gg.txt" or "y" or "n".')     
        choice = input('If you want to see the equations please type in the text file, eg: gg.txt \n Or if you like to try another equation please type (y/n)')

