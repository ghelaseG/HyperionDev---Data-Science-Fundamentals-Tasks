# calculate a user’s holiday cost including the plane cost, hotel cost, and car rental cost

#we first create a dictionary to store the cities and the prices
city_price = {"Barcelona": 100, "Milan": 120, "Mykonos": 140, "Amsterdam": 60, "Paris": 80, "Berlin": 90}

# let's get some user inputs, we use str and int for each input and capitalize for case sensitivity
city_flight = str(input(f'Please let us know which city you would like to visit, available only: {list(city_price)}: ')).capitalize()
num_nights = int(input('Please enter the number of nights you would like to stay at the hotel: '))
rental_days = int(input('Please insert the number of days you would like to hire a car: '))

# create function for each input to get the total cost and then get the total cost of the holiday

# first function, we get the price for the city selected using a for loop and a while loop in case of wrong choice
def plane_cost(city_flight):

    while True:
        for city, price in city_price.items():
            if city == city_flight:
                return price
            
        city_flight = input(f'Please try again, choosing only the available cities: {list(city_price)}: \n').capitalize()
        
# second function, we multiply the number of nights at the hotel with a random price(my choice was 60)
def hotel_cost(num_nights):

    total_hotel_cost = num_nights * 60

    return total_hotel_cost

# third function, we use different operators for discount when choosing how many days they want a car to rent
def car_rental(rental_days):
    
    if rental_days <= 10:
        price = 50
    elif rental_days >= 10 and rental_days <= 20:
        price = 40
    else:
        price = 33

    total_rental_cost = rental_days * price

    return total_rental_cost


# last function we calculate the total cost of the holiday
def holiday_cost(plane_cost, hotel_cost, car_rental):

    total_holiday_cost = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)

    return total_holiday_cost

# lastly we print out all the details about the holiday in a readable way using f string
print(f"Please find bellow the holiday details: \nCity: {city_flight}\nFlight cost: {plane_cost(city_flight)}\nNumber of nights at the hotel: {num_nights}\nHotel cost: {hotel_cost(num_nights)}\nNumber of days for car rental: {rental_days}\nCar rental cost: {car_rental(rental_days)}\nTotal holiday cost: {holiday_cost(plane_cost, hotel_cost, car_rental)}")
