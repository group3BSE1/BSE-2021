# a while loop to print da word banana starting from the last letter
fruit = 'banana'
index = (len(fruit)-1)
while index < len(fruit):
    if index >= 0:
        letter = fruit[index]
        print(letter)
        index = index - 1
    else:
        quit()