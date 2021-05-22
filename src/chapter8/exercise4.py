fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File not found , re-run and enter a valid file name')
    fhand = None
    quit()
unique = []
# reading lines in the file
for line in fhand:
    words = line.split()
    # reading each line to split it into words
    for each in words:
        exact = each.split()
        unique.append(each)
# sorting the list of unique words
unique.sort()
print(unique)
