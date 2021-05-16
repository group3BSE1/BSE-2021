# a program to count number of times letter a occurs in the word banana
def county(string, letter):
    count_x = 0
    for input_letter in string:
        if input_letter == letter:
            count_x = string.count(letter)
    return count_x
word = 'banana'
letter_x = 'a'
print(county(word, letter_x))
