list_numbers = []
while True:
    number = input('Input a number: ')
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print('Bad data')
    # storing the number in a list
    list_numbers.append(number)
    continue
print('Maximum number: ', format(max(list_numbers), '.1f'))
print('Manimum number: ', format(min(list_numbers), '.1f'))