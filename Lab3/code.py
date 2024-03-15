# a = float(input('so: '))
# print ('integer') if(a%1 == 0) else print ('not integer')
a = int(input('Input number: '))
if (a % 3 == 0 and a % 5 == 0):
    print(str(a) + ' is divisible by 3 and 5')
elif (a % 3 == 0):
    print(str(a) + ' is divisible by 3')
elif (a % 5 == 0):
    print(str(a) + ' is divisible by 5')
else: print(str(a) + ' is not divisible by 3 or 5')