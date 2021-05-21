# Reading the file measles.txt
handle = open('measles.txt', 'r')
# prompting the user to input file name and year
while True:
    fname = input('Enter file name: ')
    if fname[-4:] == '.txt':
        break
    else:
        print('Invalid file formart..use .txt')
        continue
# prompting the use untill a valid year is entered(Catching errors on years)
while True:
    year = input('Enter year: ')
    try:
        if year in "" or year == 'all' or year == 'ALL' or (len(year) <= 4 and int(year) > 0):
            break
        else:
            print('Error: Invalid year')
            continue
    except:
        print('Error! : Invalid year')
        continue
file_out = open(fname, 'w')
# line[88:93] is a slice containing the year
for line in handle:
    if line[88:93].startswith(year):
        file_out.write(line)
    elif year == "" or year.lower() == "all":
        file_out.write(line)
handle.close()
file_out.close()
quit()
