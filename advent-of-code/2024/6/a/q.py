import re

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def process_lines(lines):
    start = ()
    start_regex = '\^'
    sre = re.compile(start_regex)

    start_row = -1
    start_col = -1
    
    for row, line in enumerate(lines):
        start_index = [m.start(0) for m in sre.finditer(line)]
        if len(start_index) == 1:
            start_row = row
            start_col = start_index
            break
    
    start = (row, start_index[0], -1, 0)


    return start

def turnRight(drow, dcol):
    return (0, -drow) if dcol == 0 else (dcol, 0)

def moveDirection(curr_row, curr_col, drow, dcol):
    return (curr_row + drow, curr_col + dcol)

def checkIfGuardExits(curr_row, curr_col, drow, dcol, nbr_of_rows, nbr_of_cols):
    if drow != 0:
        next_row = curr_row + drow
        return next_row < 0 or nbr_of_rows <= next_row
    elif dcol != 0:
        next_col = curr_col + dcol
        return next_col < 0 or nbr_of_cols <= next_col
    else:
        return False

def checkIfNextIsHash(curr_row, curr_col, drow, dcol, lines):
    return lines[curr_row + drow][curr_col + dcol] == "#"

def solve(file_name):
    lines = getLines(file_name)
    nbr_of_rows = len(lines)
    nbr_of_cols = len(lines[0])
    (curr_row, curr_col, drow, dcol) = process_lines(lines)

    lines = [list(line) for line in lines]
    position = (curr_row, curr_col, drow, dcol)
    lines[curr_row][curr_col] = "X"
    while True:
        if checkIfGuardExits(curr_row, curr_col, drow, dcol, nbr_of_rows, nbr_of_cols):
            break
        elif checkIfNextIsHash(curr_row, curr_col, drow, dcol, lines):
            drow, dcol = turnRight(drow, dcol)
        else:
            curr_row, curr_col = moveDirection(curr_row, curr_col, drow, dcol)
       
        lines[curr_row][curr_col] = "X"




    count = 0
    print('....#.....\n....XXXXX#\n ....X...X.\n ..#.X...X.\n ..XXXXX#X.\n ..X.X.X.X.\n .#XXXXXXX.\n .XXXXXXX#.\n #XXXXXXX..\n ......#X..\n          ')
    for line in lines:
        print(f"{''.join(line)}'")
        for char in line:
            if char == "X":
                count += 1
    return count

if __name__ == "__main__":
    count = solve("data_real.txt")
    print(count)
