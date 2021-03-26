# a program to dispense the correct amount of change
# getting an amount to make change for
amount = float(input('Enter an amount to make change for:'))
print("Your change is...")
# giving denominations variable names
twenty_dollars = 20
ten_dollars = 10
five_dollars = 5
one_dollars = 1
quarter = 0.25
dime = 0.1
nickel = 0.05
penny = 0.01
# computing change
# calculating the twenties
twenties = int(amount // twenty_dollars)
print(twenties)
# getting remainder of the twenties
remainder_of_twenties = (amount % twenty_dollars)
# calculating the tens
tens = int(remainder_of_twenties // ten_dollars)
print(tens)
# getting reminder of the tens
remainder_of_tens = (remainder_of_twenties % ten_dollars)
# calculating the fives
fives =int(remainder_of_tens // five_dollars)
print(fives)
# getting remainder of fives
remainder_of_fives = (remainder_of_tens % five_dollars)
# calculating the ones
ones = int(remainder_of_fives // one_dollars)
print(ones)
# getting remainder of ones
remainder_of_ones = (remainder_of_fives % one_dollars)
# calculating quarters
quarters = int(remainder_of_ones // quarter)
print(quarters)
# getting remainder of quarters
remainder_of_quarters = (remainder_of_ones % quarter)
# calculating dimes
dimes = int(remainder_of_quarters // dime)
print(dimes)
# getting remainder of dimes
remainder_of_dimes = (remainder_of_quarters % dime)
# calculating nickel
nickels = int(remainder_of_dimes // nickel)
print(nickels)
# getting remainder of nickels
remainder_of_nickels = (remainder_of_dimes % nickel)
# calculating pennies
pennies = int(remainder_of_nickels // penny)
print(pennies)
# codded by group3BSE1


