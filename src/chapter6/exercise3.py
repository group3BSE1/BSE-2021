# a function to accept string and letter as arguments and compute the count
def count(words, letters):
    count_x = 0
    for letter_x in words:
        if letter_x == letters:
            count_x = count_x + 1
    print(count_x)


# calling the function
count('banana', 'a')
