a = [78, 56, 67]
b = int(input('Input new scores: '))
a.append(b)
a.sort(reverse=True)

for i, val in enumerate(a, start=1):
    print(f'{i}. {val}')
