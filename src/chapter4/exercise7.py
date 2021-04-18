def computegrade(score):
    # checking whether score is within the range of values
    if 1.0 >= score >= 0.0:
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return"B"
        elif score >= 0.7:
            return"C"
        elif score >= 0.6:
            return"D"
        else:
            return"F"
    else:
        return"Bad score"


scr = input("Enter score:")
try:
    scr = float(scr)
except:
    print("Bad score")
    exit()
print(computegrade(scr))
# scr assigns  VALUE to the parameter score

