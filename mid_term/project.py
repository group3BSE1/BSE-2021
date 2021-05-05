# repeatedly getting customer code
while True:
    code = input('Enter customer code:')
    if code == 'r' or code == 'c' or code == 'i':
        # bgn_m is the beginning meter reading
        # end_m is the ending meter reading
        bgn_m = input('Enter beginning meter reading:')
        end_m = input('Enter ending meter reading:')
        # when end_m < bgn_m, the meter reading exceeded 9 digits
        # end_m2 is what we shall use when calculating
        # trapping invalid supplied user meter readings
        try:
            bgn_m = int(bgn_m)
            end_m = int(end_m)
            if bgn_m >= 0 and end_m >= 0 and len(str(bgn_m)) <= 9 and len(str(end_m)) <= 9:
                if end_m < bgn_m:
                    end_m2 = 1000000000 + int(end_m)
                else:
                    end_m2 = end_m
            else:
                print('Invalid meter reading')
                continue
        except:
            print('Invalid meter reading')
            continue
        gallons = (int(end_m2) - int(bgn_m)) / 10
        # calculating bill for code 'r'
        if code == 'r':
            bill = format((5+(0.0005 * gallons)), ".2f")
        # calculating bill for code 'c'
        elif code == 'c':
            if gallons <= 4000000:
                bill = format(1000, ".2f")
            else:
                additional_g = gallons - 4000000
                bill = format(((0.00025 * additional_g) + 1000.00), ".2f")
        # calculating bill for code 'i'
        else:
            if gallons <= 4000000:
                bill = format(1000, ".2f")
            elif gallons <= 10000000:
                bill = format(2000, ".2f")
            else:
                exceeded_g = gallons - 10000000
                bill = format(((0.00025 * exceeded_g) + 2000), ".2f")

        print("Customer code: ", code)
        print('Beginning meter reading: ', bgn_m)
        print('Ending meter reading: ', int(end_m))
        print('Gallons of water used: ', gallons)
        print('Amount billed: '+'$'+str(bill))
        continue
    # quiting the program if customer code is invalid
    else:
        quit()
