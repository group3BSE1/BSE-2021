while True:
    fname = input('Enter file name:')
    try:
        hfile = open(fname)
        break
    except:
        hfile = None
        print('File not exist')
        continue
list_mails = []
for line in hfile:
    if line.startswith('From '):
        mails = line.split()
        list_mails.append(mails[1])
for each in list_mails:
    print(each)
print('There were', len(list_mails),'lines in the file with From as the first word')