hrs = input('Enter Hours Worked This Week: ')
rate = input('Enter Your Hourly Rate: ')
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Error, please enter numeric input')
print(h, r)
quit()
if h <= 40:
    pay = h * r
    print(pay)
else:
    pay = (40 * r) + ((h - 40)*(r * 1.5))
    print(pay)