# computing distance between two points
# getting first point from the user
x1 = float(input('Enter x value for the first point:'))
y1 = float(input(" Enter  y value for the first point:"))
# getting second point from the user
x2 = float(input(" Enter x value for the second point:"))
y2 = float(input(' Enter y value for the second point:'))
# d means distance between two points
d = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
print(d)
print(" distance between two points is "+ str(d))
# made by group3BSE1