# investment is a function that returns the final value of investment
def investment(initial, rate, time, number):
    return initial*(1 + rate/number)**(time*number)


# assigning parameters
C = int(input("Enter initial amount of investment: "))
r = float(input("Enter yearly rate: "))
t = int(input("Enter time until maturation: "))
n = int(input("Enter number of times interest is compounded : "))
p = investment(C, r, t, n)
print(p)
# coded by group3BSE


