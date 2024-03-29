food = ['ca chien']
#functions of lists
food.append('Kemchuoi')
food.remove('ca chien')
item = food.pop()
food.insert(1, 'banh canh cua')
food.sort()
food.clear()
print(item)
print(food)

drinks = ['tra sua', 'tra chanh', 'nuoc ep']
dessert = ['banh plan', 'kem']
meal= [food, drinks, dessert]
print(meal[1][2])
print(meal[2])

x = 'abc' + 'd'
x = 'abcd'

list_clone = food.copy

list1 = ['a', 'b', 7 , True]
list2 = [1, 4, 15.5]
list3 = list1 + list2 #cach1
list4 = list1.extend(list2) #cach2