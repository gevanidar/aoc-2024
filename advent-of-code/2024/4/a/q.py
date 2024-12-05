import re

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def checkHorizontal(lines, row, col):
    chars = lines[row][col:col+4]
    #print(f'H {chars=}')
    return checkChars(chars)

def checkVertical(lines, row, col):
    chars = ""
    for step in range(0, 4):
        chars += lines[row+step][col]
    #print(f'V {chars=}')
    return checkChars(chars)

def checkDownRight(lines, row, col):
    chars = ""
    for step in range(0, 4):
        chars += lines[row+step][col+step]
    #print(f'DR {chars=}')
    return checkChars(chars)

def checkDownLeft(lines, row, col):
    chars = ""
    for step in range(0, 4):
        chars += lines[row+step][col-step]
    #print(f'DL {chars=}')
    return checkChars(chars)

def checkChars(chars):
    return 1 if chars == "XMAS" or chars == "SAMX" else 0


def solve(file_name):
    lines = getLines(file_name)
    rows = len(lines)
    columns = len(lines[0])

    #print(f'Testing: {lines=} ---')
    count = 0
    for row in range(rows):
        for col in range(columns):
            #print(rows, row, columns, col)
            if col < columns - 3:
                count += checkHorizontal(lines, row, col)
            if row < rows - 3:
                count += checkVertical(lines, row, col)
                if col < columns - 3:
                    count += checkDownRight(lines, row, col)
                if 3 <= col:
                    count += checkDownLeft(lines, row, col)
            #print(count)

    return count

if __name__ == "__main__":
    count = solve("data_real.txt")
    print(count)
