import re
from itertools import product

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines


def solve(file_name, width, height):
    lines = getLines(file_name)

    newPos = []
    for row in range(height):
        tmp = []
        for col in range(width):
            tmp.append(0)
        newPos.append(tmp)
    startPos = []
    for row in range(height):
        tmp = []
        for col in range(width):
            tmp.append(0)
        startPos.append(tmp)


    for line in lines:
        p, v = line.split(" ")
        pos = re.findall(r'\d+\,\d+', p)[0]
        x, y = pos.split(",")
        velocity = re.findall(r"-{0,1}\d+\,-{0,1}\d+", v)[0]
        dx, dy = velocity.split(",")

        x = int(x)
        y = int(y)
        dx = int(dx)
        dy = int(dy)

        times = 100
        newX = (x + dx * times) % width
        newY = (y + dy * times) % height
        startPos[y][x] += 1
        newPos[newY][newX] += 1

        #print(f'{x},{y} has moved to {newX},{newY} after {dx},{dy} ({times*dx},{times*dy})')

    #print('Start----')
    #for row in startPos:
        #print(row)
    #print('New----')
    for row in newPos:
        print(row)
    midX = width // 2
    midY = height // 2

    print('--')
    northWest = [x for row in newPos[:midY] for x in row[:midX]]
    northEast = [x for row in newPos[:midY] for x in row[midX+1:]]
    print(northWest)
    print(northEast)
    southWest = [x for row in newPos[midY+1:] for x in row[:midX]]
    southEast = [x for row in newPos[midY+1:] for x in row[midX+1:]]
    print(southWest)
    print(southEast)

    sums = sum(northWest) * sum(northEast) *sum(southWest) * sum(southEast)

    return sums
    
    
if __name__ == "__main__":
    width = 101
    height = 103
    count = solve("input_a.txt", width, height)
    print(count)
