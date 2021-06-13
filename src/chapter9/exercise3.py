# prompting user to enter the file name
fname = input('Enter file name: ')
d = dict()
# catching exceptions
try:
    fhand = open(fname)
except:
    print('File does not exist')
    exit()
# reading the lines in the file
for line in fhand:
    words = line.split()
    # we only want email addresses
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        d[words[1]] = d.get(words[1], 0) + 1

print(d)