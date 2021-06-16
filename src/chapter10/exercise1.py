fname = input('Enter a file name: ')
d = dict()
try:
    fhand = open(fname)
except:
    print('File does not exist')
    quit()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        d[words[1]] = d.get(words[1], 0) + 1
t = list()
for key, val in list(d.items()):
    t.append((val, key))

t.sort(reverse=True)

for key, val in t[:1]:
    print(val, key)


