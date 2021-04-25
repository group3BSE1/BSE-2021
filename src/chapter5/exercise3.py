# 22nd April 2021
# GROUP 3
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
        amount = int(price * 100)
        # for multiple remainder = 0
        remainder = amount % 5
        if remainder == 0 and price > 0:
            print('Menu for deposits:\n')
            print(' "n" - deposit a nickel ')
            print(' "d" - deposit a dime ')
            print(' "q" - deposit a quarter ')
            print(' "o" - deposit a one dollar bill')
            print(' "f" - deposit a five dollar bill ')
            print(' "c" - cancel the purchase ')
            dollars = int(amount // 100)
            cent_s = int(amount % 100)
            print('Amount due:',dollars,' dollars and ', cent_s,' cents')
            payment = 0
            # Getting the selection from user
            while True:
                deposit = input('Indicate your selection:')
                if deposit == 'n':
                    while True:
                        payment = payment + 5
                        amount_due = amount - payment
                        # updating nickels
                        nickel = nickel + 1
                        break
                    if payment < amount:
                        print(amount_due//100,'dollars and' ,amount_due % 100, 'cents')
                        continue
                    else:
                        print('Take change')
                        break
                if deposit == 'd':
                    while True:
                        payment = payment + 10
                        amount_due = amount - payment
                        # updating dimes
                        dime = dime + 1
                        break
                    if payment < amount:
                        print(amount_due//100,'dollars and' ,amount_due % 100, 'cents')
                        continue
                    else:
                        break
                if deposit == 'q':
                    while True:
                        payment = payment + 25
                        amount_due = amount - payment
                        # updating quarters
                        quarter = quarter + 1
                        break
                    if payment < amount:
                        print(amount_due//100,'dollars and' ,amount_due % 100, 'cents')
                        continue
                    else:
                        print('Take the change')
                if deposit == 'o':
                    while True:
                        payment = payment + 100
                        amount_due = amount - payment
                        # updating ones
                        one = one + 1
                        break
                    if payment < amount:
                        print(amount_due//100,'dollars and' ,amount_due % 100, 'cents')
                        continue
                    else:
                        print('Take change')
                        break
                if deposit == 'f':
                    while True:
                        payment = payment + 500
                        amount_due = amount - payment
                        # updating fives
                        five = five + 1
                        break
                    if payment < amount:
                        print(amount_due//100,'dollars and' ,amount_due % 100, 'cents')
                        continue
                    else:
                        print('Take change')
                        break
                if deposit == 'c':
                    if payment > 0:
                        print('Please take the change below')
                        break
                    else:
                        continue
                else:
                    print('Invalid')
                    continue
            # we shall calculate the change here

        else:
            print('Illegal selection: Must be a non negative multiple of 5 cents')
        continue


