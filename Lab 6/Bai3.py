length = int(input('Input a positive number: '))
print(f'First {length} Fibonancci number(s): ')
def fibonacci(n):
    series = [0, 1]

    for i in range(2, n):
        series.append(series[i-1] + series[i-2])
    return series
list = fibonacci(length)
print(list)