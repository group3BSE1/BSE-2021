nickel = 25
dime = 25
quarter = 25
one = 0
five = 0
print(nickel, "nickel")
print(dime, "dime")
print(quarter, "quarter")
print(one, "one")
print(five, "five")
while True:
    price = input("Enter a price in digits or 'q' to quit:")
    if price == "q":
        quit()
    try:
        price = float(price)
        multiple = price * 100 % 5
        if price < 0 and multiple > 0:

    except:
        print('error')
        continue


