hours = int(input('Enter hours:'))
rate = int(input('Enter rate:'))
# extrah means extra hours
extrah = int(hours - 40)
if hours <= 40:
    pay = (hours * rate)
    print(pay)
else:
    pay2 = ((extrah * 1.5 * rate) + (hours * rate))
    print(pay2)
# group3BSE1
