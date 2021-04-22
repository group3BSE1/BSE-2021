# DAN KABAGAMBE
# TUMUSIIME FRANCIS
# NAKUYA SHAKIRAH HADIJJAH
total = 0
count = 0
smallest = None
largest = None
# Finding the largest and smallest
while True:
    a = input('Enter a number:')
    try:
        a = int(a)
        count = count + 1
        total = total + a
        if smallest is None:
            smallest = a
        else:
            if a < smallest:
                smallest = a
        if largest is None:
            largest = a
        else:
            if a > largest:
                largest = a
    except:
        if a == 'done':
            print(total)
            print(count)
            print('smallest:' , smallest)
            print("largest:", largest)

            break
        else:
            print('Invalid input')
            continue



