# computepay outputs the pay value
def computepay(hours, rate):
    if hours <= 40:
        return hours*rate
    overtime = hours-40
    return 40*rate + overtime * 1.5 * rate

hrs = input("enter hours:")
rte = input("enter rate:")
try:
    hrs = int(hrs)
    rte = float(rte)
except:
    print("Error")
print(computepay(hrs, rte))
# hours and rate are parameters

