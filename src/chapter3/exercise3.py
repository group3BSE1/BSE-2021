score = (input('Enter score:'))
try:
    score = float(score)
# scores must be between 0.0 and 1.0
    if 0.0 < score < 1.0:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print("Bad score")
except:
    score = str(score)
    print('Bad score')
    exit()


