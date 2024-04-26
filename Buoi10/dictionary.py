capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Vietnam': 'Hanoi'}
print(capitals['Vietnam'])
print(capitals.get('USA'))
capitals['China'] = ['Hello']
capitals.update({'USA' : 'ABC'})
capitals.pop('USA')
del capitals['China']

print(len(capitals))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for k, v in capitals.items():
    print(k,v)
for i in capitals:
    print(i, ':')
    print(capitals[i])
for i in capitals.values():
    print(i)