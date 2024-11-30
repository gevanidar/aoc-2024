import math

   

if __name__ == "__main__":
    primes = []
    with open('prime_file.txt', 'r') as prime_file:
        line = prime_file.readline()
        while line:
            primes.append(int(line))
            line = prime_file.readline()

    num = 600851475143

    prime = primes.pop(0)
    prime_factors = []
    while True:
        integer = num / prime
        print(f'{num}/{prime}={integer}')
        if integer == 1:
            prime_factors.append(prime)
            break
        elif num // prime == integer:
            num = integer
            prime_factors.append(prime)
        else:
            prime = primes.pop(0)
            
    i = 1
    for p in prime_factors:
        ii=i
        i *= p
        print(f'{ii}*{p}={i}')
