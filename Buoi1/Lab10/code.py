numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
num = input('Input a Roman Number:')
x = numbers.get(num)
if num in numbers :
    print(f'Arabic number: {x}')
else:
    print('Not Found')
