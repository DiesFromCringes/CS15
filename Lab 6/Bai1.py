arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Original list: ' + str(arr))
for i in range(len(arr)):
   arr[i] +=2
print(f'Add 2: {arr}')
for h in range(len(arr1)):
   arr1[h] *= 2
print(f'Multiply by 2: {arr1}')
arr2.insert(10, 0,)
arr2.pop(0)
arr2.insert(11, 1,)
arr2.pop(0)
print(f'Shift by 2: {arr2}')
