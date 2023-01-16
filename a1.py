# Assignment 1 file
# Name: Sitara Rezaee
# Student ID: 501181547

# Looking to travel to city for holiday break.
# User is asked to enter city they wish to visit and budget. Main priority is tickets, transportation, accommodation
# remaining amount in budget is amount left over for tourist activities/shopping
# Program helps user find out, based on their budget, if they can visit tourist attractions

# asking user to input name, valued inputted assigned to 'name' variable
name = input("Please enter your first and last name: ")
# print statement to greet user, informing of program
print("Hi, ", name, "! Pick a city, and based on the budget, you can find out how much can be used for activities!\n")


# function to calculate total cost of everything, with three parameters
def calculate_total_cost(plane_ticket, stay_cost, has_own_car):
    # price varies if user has a car
    if has_own_car:
        # sum of cost if they use their own car
        return plane_ticket + stay_cost
        # different total cost if they do not have a car
    else:
        # same sum as previous with additional $500 to cover transportation costs
        return plane_ticket + stay_cost + 500


# asking user to input their budget, assigned to variable 'budget'
budget = int(input("Please enter the maximum amount to be spent on the trip: "))

# as long as the budget is more than $0 the program will continue
while budget <= 0:
    # asking user to input valid number so the program continues
    print("Please enter a valid number.\n")
    # asking user again for their new budget
    budget = int(input("Please enter the maximum amount to be spent on the trip: "))
# asking which city, given three options, they want to visit, value entered assigned to variable 'city'
city = input("Enter which city you would like to travel to? \n\n Rome \n Paris \n Barcelona \n\n Answer: ")
# if the city entered is not from the provided options
while city != "Rome" and city != "Paris" and city != "Barcelona":
    # telling user to write another city rather than program stop running
    print("\nPlease choose a city from the provided options.\n")
    # new city input given 3 choices
    city = input("Enter which city you would like to travel to? \n\n Rome \n Paris \n Barcelona \n\n Answer: ")
# if user entered string 'Barcelona'
if city == "Barcelona":
    # the value of the variable plane_ticket will be 1000
    plane_ticket = 1000
# if user entered string 'Paris'
elif city == "Paris":
    # the value of the variable plane_ticket will be 2000
    plane_ticket = 2000
# if user entered string 'Rome'
elif city == "Rome":
    # the value of the variable plane_ticket will be 3000
    plane_ticket = 3000
# Telling user how much cost of plane ticket is depending on city entered
print("\nThe cost for a round trip to", city, "will be", plane_ticket, ".")
# variable 'accommodations', for the letter user inputs for where they are staying
accomodations = input(
    "\nWhere will you be staying? Answer A,B,C \n\n A. With family/friend \n B. Hotel \n C. Airbnb \n\n Answer: ")
# program converts input to uppercase, to compare strings
accomodations = accomodations.upper()
# total value defined, to be used for "accomodations == c"
total = 0
# if user inputted character A
if accomodations == "A":
    # value of stay_cost will be 0 for staying with friends
    stay_cost = 0
# if user inputs B
elif accomodations == "B":
    # cost will be 2000 for staying in hotel
    stay_cost = 2000
# if user input is C for airbnb
elif accomodations == 'C':
    # using for loop to add total cost, stop step +1, to find cost for inputted number of days
    for i in range(1, 15):
        # daily rate
        stay_cost = 60
        # sum is cost of stay for each day
        total += stay_cost
        # total cost of accomodations for airbnb is assigned to the value of total days stayed summed by for loop
        stay_cost = total
print("\nThe cost for your stay at", city, "will be:", stay_cost)

# assuming user does not have car, value of boolean is False
has_own_car = False
# asking user input, if they have a car
transportation = input("\nDo you have a car? Answer Yes/No \n Answer: ")
# if they do not input Yes or No
while transportation != ("Yes" or "yes") and transportation != ("No" or "no"):
    # asking user to print Yes or No
    print("\nPlease enter Yes or No.\n")
    # asking user to input Yes or No if they have a car
    transportation = input("Do you have a car? Answer Yes/No \n Answer: ")
# if value inputted was Yes
if transportation == "Yes":
    # the boolean expression is true
    has_own_car = True
# if they did not input Yes
else:
    # they do not have a car, so Boolean expression is false, as stated above
    has_own_car = False
# implementing the function to find total_cost
total_cost = calculate_total_cost(plane_ticket, stay_cost, has_own_car)
# Telling user total cost of trip
print("\nYour total cost for the trip is:", total_cost, ".")
# variable to find out how much they exceeded budget
other_cost = total_cost - budget
# if the user exceeded their budget, if value of total cost is more than budget
if total_cost >= budget:
    # telling user how much budget was exceeded by
    print("\nYou have exceeded your budget by ", other_cost)
# if the user did not exceed their budget
else:
    # new variable for how much money is left over for recreational activities
    remaining_budget = budget - total_cost
    # telling user how much money they have leftover
    print("\nYou have", remaining_budget, "remaining in your budget.")
