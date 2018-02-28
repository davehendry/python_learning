score = input('Please enter a numeric score between 0.0 and 1.0: ')
try:
    s = float(score)
except:
    print('Error, you did not enter a valid numeric score between 0.0 and 1.0 ')
    quit()
if s < 0.0 or s > 1.0:
    print('Error, you did not enter a valid numeric score between 0.0 and 1.0 ')
    quit()
elif s >= 0.9:
    print('A')
elif s >= 0.8:
    print('B')
elif s >= 0.7:
    print('C')
elif s >= 0.6:
    print('D')
else:
    print('F')