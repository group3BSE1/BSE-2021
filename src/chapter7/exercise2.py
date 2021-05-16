file = input('Enter the file name: ')
our_file = open(file)
count = 0
sum_of_count = 0
for line in our_file:
    if 'X-DSPAM-Confidence:' in line:
        count = count + 1
        sum_of_count = sum_of_count + float(line[-7:])
avrg = sum_of_count/count
print('Average spam Confidence:', format(avrg, '.12f'))
