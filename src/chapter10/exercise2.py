# prompting user to enter file name
fname = input('Enter a file name: ')
d = dict()
# catching exceptions
try:
    fhand = open(fname)
except:
    print('File cannot be opened!')
    quit()
# reading through the file
for line in fhand:
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue
    else:
        times = words[5].find(':')
        hours = words[5][:times]
        d[hours] = d.get(hours, 0) + 1
counts = list()
# the hours(keys) and their counts(values) are converted to list form
for key, val in list(d.items()):
    # the items from the dictionary are put in the list, counts
    counts.append((key, val))
# sort the list by the key(hours)
counts.sort()
for key, val in counts:
    print(key, val)
