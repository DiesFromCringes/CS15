def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

input_number = int(input("Input number: "))

if is_prime(input_number):
    print(f"{input_number} is a prime")
else:
    print(f"{input_number} is not a prime")