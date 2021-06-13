fhand = open('words.txt')
d = dict()
for words in fhand:
    line = words.split()
    for word in line:
        d[word] = d.get(word, 0) + 1

if 'programs' in d:
    print('True')
else:
    print('False')
