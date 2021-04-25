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
print('Welcome to vending machine change maker program')
print('Stock contains:\n')
print(nickel, "nickels")
print(dime, "dimes")
print(quarter, "quarters")
print(one, "ones")
print(five, "fives")
# Reapeatedly asking user to enter price
while True:
    price = input("Enter the purchase price (xx.xx) or `q' to quit:")
    if price == 'q':
        # will print here total before exiting!
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
                        change = payment - amount
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
                        change = payment - amount
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
                        change = payment - amount
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
                        change = payment - amount
                        break
                if deposit == 'c':
                    if payment > 0:
                        change =payment
                        break
                    else:
                        continue
                else:
                    print('Invalid')
                    continue
            # we shall calculate the change here
            print('Please take the change below')
            def q_cf():
                print(q_c, 'quarters')


            def d_cf():
                print(d_c, 'dimes')


            def n_cf():
                print(n_c, 'nickels')


            def bal_due():
                print('Machine is out of change')
                if change >= 100:
                    b_d = change // 100
                    c_d = change % 100
                    if c_d > 0:
                        print('See store manager for remaining refund.Amount due is', b_d, 'dollars and', c_d, 'cents')
                    else:
                        print('See store manager for remaining refund.Amount due is', b_d, 'dollars')
                else:
                    print('See store manager for remaining refund.Amount due is', change, 'cents')
            q_c = change//25


            if q_c > 0:
                if q_c <= quarter:
                    q_cf()
                    change = change - q_c * 25
                    d_c = change // 10
                    quarter = quarter
                    if d_c > 0:
                        if d_c <= dime:
                            d_cf()
                            dime = dime - d_c
                            change = change - d_c * 10
                        else:
                            if dime > 0:
                                print(dime, 'dimes')
                                change = change - dime * 10
                                n_c = change // 5
                                dime = dime
                                if n_c > 0:
                                    if n_c <= nickel:
                                        n_cf()
                                else:
                                    if nickel > 0:
                                        print(nickel, 'nickels')
                                        nickel = nickel
                                        change = change - nickel * 5
                                        n_c = change // 5
                                        if n_c > 0:
                                            bal_due()
                                            change = 0
                                    else:
                                        bal_due()
                            else:
                                n_c = change // 5
                                if n_c > 0:
                                    if n_c < nickel:
                                        n_cf()
                                    else:
                                        if nickel > 0:
                                            print(nickel, 'nickels')
                                            change = change - nickel * 5
                                            nickel = nickel
                                            if n_c > 0:
                                                bal_due()
                                        else:
                                            bal_due()
                                else:
                                    print('Is it here')
                                    bal_due()
                    else:  # calculating only nickes
                        n_c = change // 5
                        if n_c > 0:
                            if n_c < nickel:
                                n_cf()
                            else:
                                if nickel > 0:
                                    print(nickel, 'nickels')
                                    change = change - nickel * 5
                                    n_c = change // 5
                                    nickel = nickel
                                    if n_c > 0:
                                        bal_due()
                                        change = 0
                                else:
                                    bal_due()
                                    change = 0

                else:
                    if quarter > 0:
                        print(quarter, 'quarters')
                        change = change - quarter * 25
                        d_c = change // 10
                        quarter = quarter
                        if d_c > 0:
                            if d_c <= dime:
                                d_cf()
                                dime = dime - d_c
                                change = change - d_c * 10
                                n_c = change // 5
                                if n_c > 0:
                                    if n_c < nickel:
                                        print(n_c, 'nickels')
                                    else:
                                        if nickel > 0:
                                            print(nickel, 'nickels')
                                            change = change - nickel * 5
                                            n_c = change // 0
                                            nickel = nickel
                                            if n_c > 0:
                                                bal_due()
                                                change = 0
                                        else:
                                            bal_due()
                                            change = 0
                            else:
                                if dime > 0:
                                    print(dime, 'dimes')
                                    change = change - dime * 10
                                    n_c = change // 5
                                    dime = dime
                                    if n_c <= nickel:
                                        n_cf()
                                    else:
                                        if nickel > 0:
                                            print(nickel, 'nickels')
                                            change = change - nickel * 5
                                            n_c = change // 5
                                            nickel = nickel
                                            if n_c > 0:
                                                bal_due()
                                        else:
                                            bal_due()
                                else:
                                    n_c = change // 5
                                    if n_c > 0:
                                        if n_c < nickel:
                                            n_cf()
                                        else:
                                            if nickel > 0:
                                                print(nickel, 'nickels')
                                                change = change - nickel * 5
                                                n_c = change // 5
                                                nickel = nickel
                                                if n_c > 0:
                                                    bal_due()
                                            else:
                                                bal_due()

                        else:
                            n_c = change // 5
                            print('Not easy as u think')
                    else:
                        print('Lost here')
                        d_c = change // 10
                        if d_c > 0:
                            if d_c <= dime:
                                d_cf()
                            else:
                                if dime > 0:
                                    print(dime, 'dimes')
                                    change = change - dime * 10
                                    n_c = change // 5
                                    dime = dime
                                    if n_c > 0:
                                        if n_c < nickel:
                                            print(nickel, 'nickels')
                                            change = change - nickel * 5
                                            nickel = nickel
                                            n_c = change // 5
                                            if n_c > 0:
                                                bal_due()
                                                change = 0
                                        else:
                                            if nickel > 0:
                                                print(nickel, 'nickels')
                                                change = change - nickel * 5
                                                n_c = change // change
                                                nickel = nickel
                                                if n_c > 0:
                                                    bal_due()
                                                    change = 0
                                            else:
                                                bal_due()
                                                change = 0

                                else:
                                    n_c = change // 5
                                    if n_c > 0:
                                        if n_c < nickel and nickel > 0:
                                            n_cf()
                                        elif nickel > 0:
                                            print(nickel, 'nickels')
                                            change = change - nickel * 5
                                            nickel = nickel
                                            n_c = change // 5
                                            if n_c > 0:
                                                bal_due()
                                                change = 0
                                        else:
                                            bal_due()
            else:
                d_c = change // 10
                if d_c > 0:
                    if d_c <= dime:
                        print(d_c, 'dimes')
                        dime = dime - d_c
                        change = change - d_c * 10
                        n_c = change // 5
                        if n_c > 0:
                            if n_c <= nickel:
                                print(n_c, 'nickels')
                                change = change - n_c * 5
                                nickel = nickel - n_c
                                n_c = change // 5
                                print(n_c)
                                if n_c > 0:
                                    bal_due()
                                    change = 0
                            else:
                                bal_due()
                                change = 0
                    else:
                        print(dime, 'dimes')
                        change = change - dime * 10
                        n_c = change // 5
                        dime = dime
                        if n_c > 0:
                            if n_c <= nickel:
                                n_cf()
                            else:
                                if nickel > 0:
                                    print(nickel, 'nickels')
                                    change = change - nickel * 5
                                    nickel = nickel
                                    n_c = change // 5
                                    if n_c > 0:
                                        bal_due()
                                        change = 0
                                else:
                                    bal_due()
                else:
                    n_c = change // 5
                    if n_c > 0:
                        if n_c <= nickel:
                            n_cf()
                        else:
                            if nickel > 0:
                                print(nickel, 'nickels')
                                change = change - nickel * 10
                                n_c = change // 5
                                nickel = nickel
                                if n_c > 0:
                                    bal_due()
                                    change = 0
                            else:
                                bal_due()
                                change = 0
            # this stock will be printed at end of every transaction
        else:
            print('Illegal selection: Must be a non negative multiple of 5 cents')
        continue


