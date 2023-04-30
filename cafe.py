# let's imagine you are running a cafe and you have to do the following:

# create a list called menu, which should contain at least 4 items in the cafe
menu = ['latte', 'cappuccino', 'espresso', 'americano']

# create a dictionary called stock, which should contain the stock value for each item on your menu
stock = {'latte': 10, 'cappuccino': 12, 'espresso': 14, 'americano': 16}

# create another dictionary called price, which should contain the prices for each item on your menu
price = {'latte': 2.5, 'cappuccino': 3.5, 'espresso': 4, 'americano': 5}

# let's find out the total value for each item 
item_value = [(stock[item] * price[item]) for item in menu] #we use list comprehension to iterate through the variable menu 

# calculate the total stock worth in the cafe and print out the result

total_stock = sum(item_value) #we add all the items from the list

new_dict = dict(zip(menu, item_value)) #we create a new dictionary using zip function, with each item and the total stock
print(f"You're total stock worth in the cafe is {total_stock}, where the total for each item in the menu is {new_dict}")