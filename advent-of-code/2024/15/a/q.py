import re
from itertools import product

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines


def solve(file_name):
    lines = getLines(file_name)

    warehouse = []
    movements = []
    for index, line in enumerate(lines):
        if not line:
            continue
        elif line[0] == "#":
            warehouse.append(list(line))
        else:
            movements.append(line)
    for m in warehouse:
        print(m)
    for m in movements:
        print(m)

    start = (-1,-1)
    for row, chars in enumerate(warehouse):
        for col, char in enumerate(chars):
            if char == "@":
                start = (row, col)
                break

    movements = [move for movement in movements for move in movement]

    directions = {
        '<': (0, -1),
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0)
    }

    pos = start
    for movement in movements:
        direction = directions[movement]
        newPos = (pos[0] + direction[0], pos[1] + direction[1])
        charNewPos = warehouse[newPos[0]][newPos[1]]
        if charNewPos == "#":
            continue
        v = newPos
        charV = warehouse[v[0]][v[1]]

        while charV == "O":
            v = (v[0] + direction[0], v[1] + direction[1])
            charV = warehouse[v[0]][v[1]]
            if charV == "#": # can't move
                v = pos
                newPos = pos
                break
        while v != newPos:
            warehouse[v[0]][v[1]] = "O"
            v = (v[0] - direction[0], v[1] - direction[1])
        warehouse[pos[0]][pos[1]] = "."
        pos = newPos
        warehouse[pos[0]][pos[1]] = "@"

        if False:
            print("______________________________________________")
            print(f'Trying to move {direction} to {pos}')
            for row in warehouse:
                print(row)
            input("______________________________________________")

        
    total = 0
    for row, chars in enumerate(warehouse):
        for col, char in enumerate(chars):
            if char == "O":
                gps = 100 * row + col
                total+= gps
            
    return total

    
if __name__ == "__main__":
    data = solve("input_a.txt")
    print(data)
