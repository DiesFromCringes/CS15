# userInput = None
# while(not userInput):
#     userInput = input('Hello')
#     if (userInput == 'h'):
#         break
#     else:
#         userInput = None
#         continue
# arr = range (1, 10, 3)
# for i in arr:
#     print(i)

# import time
# for i in 'Happy New Year':
#     print(i)
#     time.sleep(1) # wait 1 sec
# print('Happy New Year')

#check number
userInput = None
while(not userInput):
    userInput = int(input('Type your number: '))
    if (userInput % 2) == 0:
        break
    else:
        userInput = None
        continuec