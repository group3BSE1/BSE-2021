# 22nd April 2021
#GROUP 3
# DAN KABAGAMBE
# TUMUSIIME FRANCIS
# NAKUYA SHAKIRAH HADIJJAH
nickel = 25
dime = 25
quarter = 25
one = 0
five = 0
print(nickel, "nickels")
print(dime, "dimes")
print(quarter, "quarters")
print(one, "ones")
print(five, "fives")
# Reapeatedly asking user to enter price
while True:
    price = input("Enter the purchase price (xx.xx) or `q' to quit:")
    if price == 'q':
        quit()
    else:
        # checking the value input from the user
        price = float(price)
        amount = price * 100
        # for multiple remainder = 0
        remainder = amount % 5
        if remainder == 0 and price > 0:
            print(price)
        else:
            print('Illegal selection: Must be a non negative multiple of 5 cents')
        continue


