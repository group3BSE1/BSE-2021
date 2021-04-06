# getting age from user
age = input('Enter age:')
try:
    age = int(age)
    if age >= 18:
        print("You can vote")
    elif age > 0:
        print(" Too young to vote")
    else:
        print('You are a time traveller')
except:
    age = str(age)
    print('Please enter only integers')
    exit()