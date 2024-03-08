# #age 
# age = int(input('Enter your age: '))
# if  (age < 0 ):
#     print('Not born')
# elif(age < 18):
#     print('teen')
# elif(age < 60):
#     print('adult')
# else:
#     print('old')

#boolean
a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)

#keo bua bao
import random
list_str = ['keo', 'bua', 'bao']

def randomSkill(list_skill):
    return random.choice(list_skill)
userInput = input('keo bua or bao: ')
machineInput = randomSkill(list_str)
def checkResult(user, machine):
    if (user == 'keo' and machine == 'keo'):
        print('hoa')
        return
    elif(user == 'bao' and machine == 'keo'):
        print('thua')
        return
    elif(user == 'keo' and machine == 'bua'):
        print('thua') 
        return
    elif(user == 'bao' and machine == 'bao'):
        print('hoa')
        return
    elif(user == 'bao' and machine == 'bua'):
        print('thang')
        return
    elif(user == 'bua' and machine == 'keo'):
        print('thang')
        return
    elif(user == 'bua' and machine == 'bua'):
        print('hoa')
        return
    elif(user == 'bua' and machine == 'bao'):
        print('thua')
        return
    elif(user == 'keo' and machine == 'bao'):
        print('thang')
        return
checkResult(user=userInput, machine=machineInput)
print(machineInput)
