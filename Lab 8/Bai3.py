def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def prime(n):
    count = 0
    number = 2
    primes = []
    while count < n:
        if is_prime(number):
            primes.append(number)
            count += 1
        number += 1
    return primes

n = int(input("Input number: "))
primes = prime(n)
print(f"First {n} prime(s): {' '.join(map(str, primes))}")