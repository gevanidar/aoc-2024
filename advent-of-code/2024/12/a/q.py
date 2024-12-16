import re
from itertools import product

    

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [list(l.strip()) for l in f.readlines()]
    return lines

def solve(file_name):
    lines = getLines(file_name)
    rows = len(lines)
    cols = len(lines[0])

    found = []
    row = 0
    col = 0
    clusters = []
    #print(rows*cols)
    while True:
        position = (row, col)
        if position in found:
            if col + 1 < cols:
                col += 1
            else:
                col = 0
                row += 1
            #print(col, cols, row, rows)
            if col+1 == cols and row+1 == rows:
                break
        else:
            cluster = search(lines, position)
            found.extend(cluster.positions)
            print(cluster.char, cluster.perimiter, cluster.getArea(), cluster.positions)
            clusters.append(cluster)

    #print(found)

    total = 0
    for cluster in clusters:
        total += cluster.getPrice()
        print(f'A region of {cluster.char} plants with price {cluster.getArea()} * {cluster.perimiter}={cluster.getPrice()}')

    return total
        
def search(lines, position):
    row = position[0]
    col = position[1]
    char = lines[position[0]][position[1]]
    cluster = Cluster(char, 0, position)

    neighbours = []
    # If I scroll right and down these might be unecessary?
    if 0 < col:
        west = lines[row][col-1]
        if char == west:
            expand(lines, cluster, (row, col - 1))
        else:
            cluster.addPerimiter(1)
    elif col == 0:
        cluster.addPerimiter(1)
    if 0 < row:
        north = lines[row-1][col]
        if char == north:
            expand(lines, cluster, (row-1, col))
        else:
            cluster.addPerimiter(1)
    elif row == 0:
        cluster.addPerimiter(1)
    if col + 1 < len(lines[0]):
        east = lines[row][col+1]
        if east == char:
            expand(lines, cluster, (row, col+1))
        else:
            cluster.addPerimiter(1)
    elif col + 1 == len(lines[0]):
        cluster.addPerimiter(1)
    if row + 1 < len(lines):
        south = lines[row+1][col]
        if south == char:
            expand(lines, cluster, (row+1, col))
        else:
            cluster.addPerimiter(1)
    elif row + 1 == len(lines):
        cluster.addPerimiter(1)

    return cluster
            
def expand(lines, cluster, position):
    row = position[0]
    col = position[1]
    char = cluster.char
    if position in cluster.positions:
        return
    cluster.addPosition(position)
    #print(f'{cluster.char}, {cluster.perimiter} {position}')
    if 0 < col:
        west = lines[row][col-1]
        if char == west:
            expand(lines, cluster, (row, col-1))
        else:
            cluster.addPerimiter(1)
    else:
        cluster.addPerimiter(1)
    #print(f'w-{cluster.char}, {cluster.perimiter} {position}')
    if 0 < row:
        north = lines[row-1][col]
        if char == north:
            expand(lines, cluster, (row-1, col))
        else:
            cluster.addPerimiter(1)
    else:
        cluster.addPerimiter(1)
    #print(f'n-{cluster.char}, {cluster.perimiter} {position}')
    if col + 1 < len(lines[0]):
        east = lines[row][col+1]
        if east == char:
            expand(lines, cluster, (row, col+1))
        else:
            cluster.addPerimiter(1)
    else:
        cluster.addPerimiter(1)
    #print(f'e-{cluster.char}, {cluster.perimiter} {position}')
    if row + 1 < len(lines):
        south = lines[row+1][col]
        if south == char:
            expand(lines, cluster, (row+1, col))
        else:
            cluster.addPerimiter(1)
    else:
        cluster.addPerimiter(1)
    #print(f's-{cluster.char}, {cluster.perimiter} {position}')


class Cluster:
    def __init__(self, char, perimiter, position):
        self.char = char
        self.perimiter = perimiter
        self.positions = [position]

    def addPerimiter(self, perimiter):
        self.perimiter += perimiter

    def getArea(self):
        return len(self.positions)

    def addPosition(self, position):
        if position not in self.positions:
            self.positions.append(position)

    def getPrice(self):
        return self.perimiter * self.getArea()

if __name__ == "__main__":
    count = solve("input_a.txt")
    print(count)
