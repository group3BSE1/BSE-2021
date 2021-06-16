fname = input('Enter filename: ')
d = dict()
try:
    fhand = open(fname)
    for line in fhand:
        words = line.split()
        if len(words) < 3 or words[0] != 'From':
            continue
        else:
            d[words[2]] = d.get(words[2], 0) + 1
    print(d)
except:
    print('File does not exist')
    exit()



