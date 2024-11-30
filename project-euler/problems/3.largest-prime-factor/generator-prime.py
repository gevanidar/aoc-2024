import math

def checkIfPrime(primes, new_prime):
    max_check = math.sqrt(new_prime)

    for prime in primes:
        #print(f'{new_prime / prime=} == {new_prime // prime=}')
        if prime >= max_check:
            return True
        if new_prime / prime == new_prime // prime:
            return False
    return True
    

if __name__ == "__main__":
    primes = []
    # Load
    with open('prime_file.txt', 'r') as prime_file:
        #print(f'Loading Primes:')
        line = prime_file.readline()
        while line:
            primes.append(int(line))
            line = prime_file.readline()
        #print(primes)

    # Append
    new_prime = primes[-1]
    with open('prime_file.txt', 'a') as prime_file:
        #print(f'Finding new primes:')

        num = 600851475143
        max_num = math.sqrt(num)
        #print(f'sqrt({num})={max_num}')
        while True:
            new_prime += 2
            #print(f'Checking: {new_prime=}')
            if checkIfPrime(primes, new_prime):
                #print(f'{new_prime=} is a prime')
                primes.append(new_prime)
                prime_file.write(f'{new_prime}\n')
            if new_prime > max_num:
                break

