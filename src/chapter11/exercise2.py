import re
# requesting user for input
fname = input('Enter file: ')
# catching exceptions
try:
    fhand = open(fname)
except:
    print('File cannot be opened')
    exit()

listy = list()
# reading through the open file
for line in fhand:
    line = line.rstrip()
    # extracting the number from the line
    number = re.findall('^New Revision: ([0-9.]+)', line)
    if len(number) > 0:
        for digit in number:
            digit = float(digit)
        listy.append(digit)

average = sum(listy)/len(listy)
print(int(average))

