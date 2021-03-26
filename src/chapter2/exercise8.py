# Defining initial amount
# C is initial investment
C = float(input("Enter initial investiment amount C:"))
# r is yearly rate
r = float(input("enter rate in the decimal r: "))
# n is number of times the interest is compounded per year
n = int(input("Enter the number of times interest is compounded n:"))
# t is the number of years until maturation
t = int(input("enter the years until maturation t: "))
# p is the final amount got after  investmentss
p = C * (1 + (r/n)) ** (t * n)
# answer rounded to the nearest penny
answer = round(p, 2)
print(answer)
# coded by group3BSE1 copyright 2021
