student = ('Diep', 25, 'female', 'Diep')
print(student)

print(student.count('Diep'))
print(student.index('female'))

for i, val in enumerate(student, start=1):
    print(f'{i}. {val}')

if 'Diep' in student:
    print('True')

number = (22, 3, 4, 18.5, 6, 8, 20, 680)
number[1:3]
number[::3]
number[::-1]