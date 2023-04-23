# create a program that allows the user to access two different financial calculators:
# an investment calculator and a home loan repayment calculator

import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print(" ")

choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()

while True: 
    if choice.lower() == 'exit':
          break
    
    elif choice != 'investment' and choice != 'bond':
          choice = input("Please try again!\nIf you wish to exit the application please enter 'exit'.\nOtherwise please enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()
    
    elif choice == 'investment':
          amount_invested = float(input('Please enter the amount of money you want to deposit:\n'))
          interest_rate = float(input('Please enter at what interest rate(only the number):\n'))
          interest_rate = interest_rate / 100
          number_years = int(input('Please enter the number of years you plan to invest:\n'))
          
          interest_choice = input('Please enter if you would like \"simple\" or \"compound\" interest:\n').lower()
          interest = []

          while True:

            if interest_choice != 'simple' and interest_choice != 'compound':
                interest_choice = input('Please enter if you would like \"simple\" or \"compound\" interest:\n').lower()   
            else:
                interest.append(interest_choice)

                for i in interest:
                    if i == 'simple':
                        total_simple_interest = amount_invested*(1 + interest_rate*number_years)
                        print(f"You're total simple interest is: {total_simple_interest}")
                        break
                    elif i == 'compound':
                        total_compound_interest = amount_invested * math.pow((1+interest_rate), number_years)
                        print(f"You're total compound interest is: {total_compound_interest}.")
                        break
            break
          
    elif choice == 'bond':
        house_value = int(input('Please enter the current value of the house:\n'))
        house_interest = float(input('Please enter the interest rate(only the number):\n'))
        months_payment = int(input('Please enter the number of months you plan to take to repay the bond:\n'))

        house_interest = (house_interest / 100) / 12
        total_money_repay = (house_interest * house_value)/(1 - (1 + house_interest)**(-months_payment))
        print(f"The total amount you'll have to repay each month is {total_money_repay}")
    break
                                
                                

                        

