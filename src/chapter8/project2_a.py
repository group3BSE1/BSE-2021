# Reading the file measles.txt
handle = open('measles.txt', 'r')
# prompting the user to input file name and year
fname = input('Enter file name: ')
year = input('Enter year: ')
file_out = open(fname, 'w')
for line in handle:
    if line[88:93].startswith(year):
        file_out.write(line)
    elif year == "" or year.lower() == "all":
        file_out.write(line)
handle.close()
file_out.close()
quit()
