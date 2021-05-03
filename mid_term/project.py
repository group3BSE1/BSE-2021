# repeatedly getting customer code
while True:
    code = input('Enter customer code:')
    if code == "r" or code == "c" or code == "i":
        # bgn_m is the beginning meter reading
        # end_m is the ending meter reading
        bgn_m = input('Enter beginning meter reading:')
        end_m = input('Enter ending meter reading:')
        # when end_m < bgn_m, the meter reading exceeded 9 digits
        # end_m2 is what we shall use when calculating
        if end_m < bgn_m:
            end_m2 = 1000000000 + int(end_m)
        else:
            end_m2 = end_m
        gallons = (int(end_m2) - int(bgn_m))/10
        print("Customer code: ", code)
        print('Beginning meter reading: ', bgn_m)
        print('Ending meter reading: ', int(end_m))
        print('Gallons of water used: ', gallons)
        continue
    # quiting the program if customer code is invalid
    else:
        quit()
