hours = input('Enter hours:')
try:
    hours = int(hours)
except:
    print('Error, please a numeric input')
    exit()
rate = input('Enter rate:')
try:
    rate = int(rate)
except:
    print('Error, please a numeric input')
    exit()
# extrah means extra hours
extrah = int(hours - 40)
if hours <= 40:
    pay = (hours * rate)
    print(pay)
else:
    pay2 = ((extrah * 1.5 * rate) + (hours * rate))
    print(pay2)
# group3BSE1
