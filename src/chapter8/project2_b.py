global file_object
global min_country
global max_country


def open_file():
    global file_object
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


def process_file(file_object_p):
    # getting user inputs
    global min_country, max_country
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
    list_criteria = []
    for line in file_object_p:
        # line[88:93] is the slice having the year and line[51:57] is one having the income level
        if line[88:93].startswith(year) and ilevel in line[51:57]:
            count = count + 1
            # percent_no is a variable to hold the percentage value
            percent_no = line[59:61]
            list_criteria.append(line)
            # putting the percentages in a list
            percentages.append(int(percent_no))
            max_country = str(max(percentages))
            min_country = str(min(percentages))
    # catching an error when the year is not found in  the file i.e when list_criteria is empty
    if len(list_criteria) < 1:
        print('Error: The year does not match any record!')
        quit()
    list_max_countries_nw = []
    list_min_countries_nw = []
    for line in list_criteria:
        if max_country in line:
            list_max_countries_nw.append(line[:45])
    for line in list_criteria:
        if min_country in line:
            list_min_countries_nw.append(line[:45])

    # a function to get the most frequent country with max or min percentage
    def most_frequent_country(list_country):
        counter = 0
        country_name = list_country[0]
        for i in list_country:
            current_frequency = list_country.count(i)
            if current_frequency > counter:
                counter = current_frequency
                country_name = i
        return country_name
    country_most = most_frequent_country(list_max_countries_nw)
    countryless = most_frequent_country(list_min_countries_nw)

    # Displaying a report to the user
    print('\nA report for the matching criteria')
    print('Count of records: ', count)
    print('Average percentage of children vaccinated: ', format((sum(percentages)/count), ".1f"))
    print('Maximum percentage: ', max(percentages), ' in', country_most)
    print('Minimum percentage: ', min(percentages), ' in', countryless)

# a function to invoke the open_file and process_file functions


def main():
    process_file(open_file())
    file_object.close()


main()
