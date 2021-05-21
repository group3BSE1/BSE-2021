def open_file():
    while True:
        # repeatedly prompting for a file name until if its valid
        file_name = input('Enter the file name: ')
        # checking if file can be opened
        try:
            file_object = open(file_name)
            break
        except:
            print('Error: file not Found')
            file_object = None
            continue
    return file_object


def process_file(file_object):
    # getting user inputs
    year = input('Enter the year: ')
    while True:
        income_level = input('Enter income level:')
        try:
            income_level = int(income_level)
            if income_level <= 4:
                break
            else:
                print('Error')
                continue
        except:
            print('Error')
            continue
    leves = ['WB_LI', 'WB_LMI', 'WB_UMI', 'WB_HI']
    ilevel = leves[income_level - 1]
    count = 0
    percentages = []
    for line in file_object:
        # line[88:93] is the slice having the year and line[51:57] is one having the income level
        if line[88:93].startswith(year) and ilevel in line[51:57]:
            count = count + 1
            # percent_no is a variable to hold the percentage value
            percent_no = line[59:61]
            # putting the percentages in a list
            percentages.append(int(percent_no))



def main():
    process_file(open_file())
