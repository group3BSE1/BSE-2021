fname = input('Enter file name: ')
d = dict()
try:
    fhand = open(fname)
except:
    print('File cannot be opened')
    exit()
for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        d[words[1]] = d.get(words[1], 0) + 1
# code to get the maximum messages
largest = 0
for email in d:
    # the d[email] gets the value of the key, email that is why it's an integer
     if d[email] > largest:
        # the email address is stored in the variable largest_e
        largest_e = email
        # if the above condition is true, then the largest becomes the value, d[email]
        largest = d[email]
print(largest_e, largest)