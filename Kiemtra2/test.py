a = [0]
sum = 0
b = int(input('Input the list of numbers: '))
a.append(b)
print(a)
if b == 0:
    for i in range(len(a)):
        sum = sum + a[i]
        print(f'Sum of all numbers: {sum}') 