# a program to open a file and print its contents line by line
file = input("Enter a file name: ")
fhand = open(file)
for line in fhand:
    line_output = line.upper()
    print(line_output.strip())
