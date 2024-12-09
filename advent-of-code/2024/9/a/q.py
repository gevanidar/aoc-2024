import re
from itertools import product


def getLine(file_name):
    line = []
    with open(file_name, 'r') as f:
        line = [l.strip() for l in f.readline()]
    return line

def solve(file_name):
    line = getLine(file_name)
    digits = []
    spaces = []
    new_index = 0

    for index, num in enumerate(line):
        if not num:
            break
        num = int(num)
        new_indices = []
        for i in range(num):
            new_indices.append(new_index)
            new_index += 1
        if index % 2 == 0:
            digits.append(new_indices)
        else:
            spaces.extend(new_indices)

    row = len(digits) - 1
    #print(row)
    #print(digits)
    for space in spaces:
        length = len(digits[row]) - 1
        for index, digit in enumerate(digits[row][::-1]):
            if space < digit:
                digits[row][length-index] = space
                if index == length:
                    row -= 1
                break
        
    checksum = 0
    for index, row in enumerate(digits):
        for val in row:
            #print(index, val)
            value = index * val
            checksum += value
    return checksum
    
    
if __name__ == "__main__":
    count = solve("input_a.txt")
    print(count)
