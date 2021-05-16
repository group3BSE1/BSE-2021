# prompting for a file name
file_name = input('Enter the file name:')
try:
    f_open = open(file_name)
    x = 0
    if file_name == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!'")
    for line in f_open:
        if line.startswith('Subject:'):
            x = x + 1
    print('There were ', x, 'subject lines in', file_name)
# when the file cannot be opened
except:
    if file_name == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!'")
    else:
        print('File cannot be opened: ', file_name)
    quit()
