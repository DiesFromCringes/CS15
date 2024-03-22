
print('-- Registration --')
name = input('Username: ')
while True:
     password = int(input('Password: '))
     repeat = int(input('Repeat password: '))
     if repeat == password :
        break
     else:
         print('Invalid password. Please input again')
         continue
while True:
    email = input('Email: ') 
    if email.find('@') == -1:
        print('Invalid email')
    elif email.find('.') == -1:
        print('Invalid email')
    elif email.isdigit():
        print('Invalid email')
    elif email.isalpha():
        print('Invalid email')
    elif len(email) <= 8:
         print('Invalid email')
    else:
       print('Register successfully')
       break

