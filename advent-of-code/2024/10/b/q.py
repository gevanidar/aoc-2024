import re
from itertools import product

class Node:
    def __init__(self, row, col, value):
        self.val= value
        self.col = col
        self.row = row
        self.neighbours = []
    def addNeighbour(self, node):
        self.neighbours.append(node)



def convertToNodes(lines):
    nodeLines = []
    for row, line in enumerate(lines):
        nodeLine = []
        for col, val in enumerate(line):
            row = int(row)
            col = int(col)
            val = int(val)
            node = Node(row, col, val)
            nodeLine.append(node)
        nodeLines.append(nodeLine)
    return nodeLines
    

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [list(l.strip()) for l in f.readlines()]
    lines = convertToNodes(lines)
    return lines

def traverse(lines, node, num, endNodes):
    if num == 10:
        endNodes.append(node)
        return
    row = node.row
    col = node.col
    #print(f'{node.val} {num=}, ({col},{row})')
    rows = len(lines)
    cols = len(lines[0])
    up = row - 1
    if 0 <= up:
        upNode = lines[up][col]
        if num == upNode.val:
            #print("UP")
            #print(f'{upNode.val} {num=}, ({upNode.col},{upNode.row})')
            node.addNeighbour(upNode)
            traverse(lines, upNode, num + 1, endNodes)
    down = row + 1
    if down < rows:
        downNode = lines[down][col]
        if num == downNode.val:
            #print("DOWN")
            #print(f'{downNode.val} {num=}, ({downNode.col},{downNode.row})')
            node.addNeighbour(downNode)
            traverse(lines, downNode, num + 1, endNodes)
    right = col + 1
    if right < cols:
        rightNode = lines[row][right]
        if num == rightNode.val:
            #print("RIGHT")
            #print(f'{rightNode.val} {num=}, ({rightNode.col},{rightNode.row})')
            node.addNeighbour(rightNode)
            traverse(lines, rightNode, num + 1, endNodes)
    left = col - 1
    if 0 <= left:
        leftNode = lines[row][left]
        if num == leftNode.val:
            #print("LEFT")
            #print(f'{leftNode.val} {num=}, ({leftNode.col},{leftNode.row})')
            node.addNeighbour(leftNode)
            traverse(lines, leftNode, num + 1, endNodes)

    return endNodes

def solve(file_name):
    lines = getLines(file_name)

    #print(lines)
    
            
    start = Node(-1,-1,-1)
    end = Node(-1,-1,10)
    endNodes = []
    for row, line in enumerate(lines):
        for col, node in enumerate(line):
            if node.val == 0:
                start.addNeighbour(node)
                ends = []
                traverse(lines, node, 1, ends)
                endNodes.append(ends)
                #input("test")


    #print(endNodes)


    total = 0
    positions = []
    for trailHeads in endNodes:
        for node in trailHeads:
            position = (node.row, node.col)
            positions.append(position)
                #print(node.val, node.row, node.col)

        total += len(positions)
    #print(positions)


    return len(positions)
    
if __name__ == "__main__":
    count = solve("input_b.txt")
    print(count)
