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
