# DAN KABAGAMBE
# TUMUSIIME FRANCIS
# NAKUYA SHAKIRAH HADIJJAH
total = 0
count = 0
average = 0
# forming a loop
while True:
    a = input('Enter a number:')
    try:
        a = int(a)
        count = count + 1
        total = total+a
        average = total / count
    except:
        if a == 'done':
            print(total)
            print(count)
            print(average)
            break
        else:
            print('Invalid input')
            continue



