# Defining decisions to display to the user
reject = "No thanks , I can find something better"
accept = "Sure, I can work with this"
kla = "No way"
spac = 'Space'
mbra = 'Mbarara'
kamp = "Kampala"
# Prompting for location from user
location = input("Location:")
# Prompting pay from a user
pay = input("Pay:")
# using conditions to take decisions depending on user inputs
try:
    location = str(location)
    pay = int(pay)
    if location.lower() == mbra.lower():
        if pay > 4000000:
            print(accept)
        else:
            print(reject)
    elif location.lower() == kamp.lower():
        if pay >= 10000000:
            print(accept)
        else:
            print(kla)
    elif location.lower() == spac.lower():
        print(accept)
    else:
        if pay >= 6000000:
            print(accept)
        else:
            print(reject)
except:
    pay = str(pay)
    print("Pay must be a number")
    exit()
# group3BSE1