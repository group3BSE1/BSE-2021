fname = input('Enter a file name: ')
d = dict()
# catching exceptions
try:
    fhand = open(fname)
except:
    print('File cannot be opened')
    exit()
# reading through the file
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if line.startswith('From '):
        # we store the words in the second position to the variable called email
        email = words[1]
        #  we  split the email and then [1] returns the second item
        domain = email.split('@')[1]
        d[domain] = d.get(domain, 0) + 1
print(d)
