# repeatedly getting customer code
while True:
    code = input('Enter customer code:')
    if code == "r" or code == "c" or code == "i":
        print("Customer code: ", code)
        continue
    # quiting the program if customer code is invalid
    else:
        quit()

