fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug', words
    if len(words) == 0:continue
    if words[0] != 'From': continue
    if len(words) >=3:
        print(words[2])  # this line can cause the program to fail if not guarded against
    else:
        print('Error')
        quit()