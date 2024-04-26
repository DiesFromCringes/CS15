# factorial = 1
# num = int(input('Input a number: '))
# if num < 0 :
#     print('Factorial does not exist')
# elif num == 0:
#     print('0! = 1')
# else:
#     for i in range (1, num + 1):
#         factorial = factorial*i
#     print(f'{num}! = {factorial}')


#2
# array = [5, 1, 8, 92, -1, 30]

# def sort(arr):
#     arr.pop(0)  
#     arr.insert(1, 5)
#     arr.pop(3)
#     arr.insert(5, 92)
#     arr.pop(3)
#     arr.insert(0, -1)
#     return arr
# print(sort(array))


#3
# length = int(input('Input a positive number: '))
# print(f'First {length} Fibonancci numbers: ')
# def fibonacci(n):
#     series = [0, 1]

#     for i in range(2, n):
#         series.append(series[i-1] + series[i-2])
#     return series
# list = fibonacci(length)
# print(list) 