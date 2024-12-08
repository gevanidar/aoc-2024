import re
from itertools import product


def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def process_lines(lines):
    tower_maps = {}
    p = re.compile("[A-Za-z0123456789]")

    for row,line in enumerate(lines):
        for m in p.finditer(line):
            char = m.group() 
            col = m.start()
            #print(f"{char=} at position {row},{col}")
            if char in tower_maps:
               tower_maps[char].append((row, col))
            else:
               tower_maps[char] = [(row, col)]

    return tower_maps

def checkAntiNode(p, dx, dy, rows, cols):
    anti_nodes = []
    a1 = (p[0] - dx , p[1] - dy)
    while 0 <= a1[0] and a1[0] < rows and 0 <= a1[1] and a1[1] < cols:
        anti_nodes.append(a1)
        a1 = (a1[0] - dx , a1[1] - dy)
    return anti_nodes


def solve(file_name):

    lines = getLines(file_name)
    rows = len(lines)
    cols = len(lines[0])
    tower_maps = process_lines(lines)
    anti_nodes = []
    for char, positions in tower_maps.items():
        #print(char, positions)
        for index, p1 in enumerate(positions):
            for p2 in positions[index+1:]:
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]

                new_anti_nodes_1 = checkAntiNode(p1, -dx, -dy, rows, cols)
                for new_anti_node in new_anti_nodes_1:
                    if new_anti_node not in anti_nodes:
                        anti_nodes.append(new_anti_node)

                new_anti_nodes_2 = checkAntiNode(p2, dx, dy, rows, cols)
                for new_anti_node in new_anti_nodes_2:
                    if new_anti_node not in anti_nodes:
                        anti_nodes.append(new_anti_node)
                    

                #print(dx, dy, a1, a2)
                
    #print(len(anti_nodes))
    return len(anti_nodes)
    
    
if __name__ == "__main__":
    count = solve("input_b.txt")
    print(count)
