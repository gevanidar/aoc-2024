import re

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def checkCrossMAS(lines, row, col):
    dl = lines[row-1][col-1] + lines[row+1][col+1]
    dr = lines[row-1][col+1] + lines[row+1][col-1]
    #print(f'{lines[row][col]=}{dl=}, {dr=}')
    if lines[row][col] != "A": 
        return 0
    dl = lines[row-1][col-1] + lines[row+1][col+1]
    dr = lines[row-1][col+1] + lines[row+1][col-1]
    return checkChars(dl, dr)

def checkChars(dl, dr):
    return 1 if (dl == "MS" or dl == "SM") and (dr == "MS" or dr == "SM") else 0


def solve(file_name):
    lines = getLines(file_name)
    rows = len(lines)
    columns = len(lines[0])

    #print(f'Testing: {lines=} ---')
    count = 0
    for row in range(1,rows-1):
        for col in range(1,columns-1):
            #print(row, col)
            count += checkCrossMAS(lines, row, col)

    return count

if __name__ == "__main__":
    count = solve("data_real.txt")
    print(count)
