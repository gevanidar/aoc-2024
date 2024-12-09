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
            if new_indices:
                spaces.append(new_indices)


    nbr_of_rows = len(digits)
    for index, rows in enumerate(digits[::-1]):
        length = len(rows)
        for space_index, space in enumerate(spaces):
            nbr_of_spaces = len(space)
            #print(rows, length, space, nbr_of_spaces)
            if length <= nbr_of_spaces:
                print(f'old: {rows=}\n{space=}')
                if space[0] < digits[nbr_of_rows - 1 - index][0]:
                    digits[nbr_of_rows - 1 - index] = space[:length]
                    spaces[space_index] = space[length:]
                print(f'new: {digits[nbr_of_rows - 1 - index]=}\n{spaces[space_index]=}')
                break

        if index + 10 > nbr_of_rows:
            input("-----")
        

    checksum = 0
    for index, row in enumerate(digits):
        for val in row:
            #print(index, val)
            value = index * val
            checksum += value
    return checksum
    
    
if __name__ == "__main__":
    count = solve("input_b.txt")
    print(count)
