import re
# prompting user to enter a regular expression which must be a string
reg = str(input('Enter a regular expression: '))
fhand = open('mbox.txt')
# initialize count
count = 0
for line in fhand:
    line = line.rstrip()
    if re.search(reg, line):
        count = count + 1
print('mbox.txt', 'had', str(count), 'lines that matched', reg)