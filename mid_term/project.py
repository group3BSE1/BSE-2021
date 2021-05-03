# repeatedly getting customer code
while True:
    code = input('Enter customer code:')
    if code == "r" or code == "c" or code == "i":
# bgm_m is the beginning meter reading
# end_m is the ending meter reading
        bgn_m = input('Enter beginning meter reading:')
        end_m = input('Enter ending meter reading:')
        print("Customer code: ", code)
        print('Beginning meter reading: ', bgn_m)
        print('Ending meter reading: ', end_m)
        continue
    # quiting the program if customer code is invalid
    else:
        quit()

