fhand = open('words.txt')
d = dict()
for line in fhand:
    words = line.split()
    for word in words:
        d[word] = d.get(word, 0) + 1

if 'programs' in d:
    print('True')
else:
    print('False')
