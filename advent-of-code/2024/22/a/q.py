import re
from itertools import permutations

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [int(l.strip()) for l in f.readlines()]
    return lines

def solve(file_name):
    """
    In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:

        Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
        Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
        Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.

    Each step of the above process involves mixing and pruning:

        To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
        To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
    """
    
    lines = getLines(file_name)


    test = True
    if (test):
        print('Test start ---')
        secret = 123
        expectedSecrets = [ 15887950, 16495136, 527345, 704524, 1553684, 12683156, 11100544, 12249484, 7753432, 5908254 ]
        index = 0
        while index < len(expectedSecrets):
            secret = operationBit(secret)
            expected = expectedSecrets[index]
            print(f'{secret=} == {expected=} -> {secret == expected}')
            index += 1
        print('Test over ---')

    newSecrets = []
    for secret in lines:
        newSecret = secret
        for i in range(2000):
            newSecret = operationBit(newSecret)
        newSecrets.append(newSecret)


    print(newSecrets)
    return sum(newSecrets)

def operationBit(secret):
    result = secret << 6
    secret = mix(secret, result)
    secret = prune(secret)
    result = int(secret >> 5)
    secret = mix(secret, result)
    secret = prune(secret)
    result = secret << 11
    secret = mix(secret, result)
    secret = prune(secret)
    return secret

def operation(secret):
    result = secret * 64
    secret = mix(secret, result)
    secret = prune(secret)
    result = int(secret / 32)
    secret = mix(secret, result)
    secret = prune(secret)
    result = secret * 2048
    secret = mix(secret, result)
    secret = prune(secret)
    return secret

def mix(secret, result):
    return secret ^ result

def prune(secret):
    return secret % 16777216

    
if __name__ == "__main__":
    data = solve("input_a.txt")
    print(data)

    
