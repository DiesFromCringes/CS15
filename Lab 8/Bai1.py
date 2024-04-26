def is_int(num):
    return num.is_integer()
number = float(input("Input number: "))
if is_int(number):
    print(f'{int(number)} is an integer')
else:
    print(f'{number} is not an integer')