# investment is a function that returns the final value of investment
def investment(initial, rate, time, number):
    return initial*(1 + rate/number)**(time*number)


# assigning parameters
C = input("Enter initial amount of investment: ")
r = input("Enter yearly rate: ")
t = input("Enter time until maturation: ")
n = input("Enter number of times interest is compounded: ")
p = investment(C, r, t, n)
try:
    C = int(C)
    r = float(r)
    t = int(t)
    n = int(n)
except:
    print('Please Enter Numeric Character:')
    exit()

print(p)
# coded by group3BSE


