import string
# prompting user for file name
fname = input('Enter a file name: ')
d = dict()
# initialise count
counts = 0
# catching exceptions
try:
    fhand = open(fname)
except:
    print('Invalid input')
    exit()

for line in fhand:
    line = line.lower()
    line = line.strip()
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()

    for word in words:
        for letter in word:
            # count every letter for relative frequencies
            counts += 1
            d[letter] = d.get(letter, 0) + 1

lst = list()
for key, val in list(d.items()):
    # we update the list with the relative frequency and its key(letter)
    lst.append((val/counts, key))
# sorts in decreasing frequency starting from highest to lowest
lst.sort(reverse=True)

for key, val in lst:
    print(key, val)