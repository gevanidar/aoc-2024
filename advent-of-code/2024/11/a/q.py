import re
from itertools import product


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def setLeft(node):
        self.left = node
        
    def setRight(node):
        self.right = node

def generateNextNode(S, node):
    val = node.val
    if val == 0:
        if 1 not in S:
            node.left = Node(1)
            S[1] = node.left
        if S[0].left == None:
            node.left = S[1]
        return [S[1]]

    sval = str(val)
    length = len(sval)
    if length % 2 == 0:
        mid = length // 2
        left = int(sval[:mid])
        if left not in S:
            node.left = Node(left)
            S[left] = node.left
        if node.left == None:
            node.left = S[left]
        right = int(sval[mid:])
        if right not in S:
            node.right = Node(right)
            S[right] = node.right
        if node.right == None:
            node.right = S[right]
        return [S[left], S[right]]

    nval = val * 2024
    if nval not in S:
        node.left = Node(nval)
        S[nval] = node.left
    if node.left == None:
        node.left = S[nval]
    return [S[nval]]

def getAtSteps(S, P, steps):
    values = P
    while True:
        newValues = []
        for value in values:
            node = S[value]
            if not node.left:
                t = generateNextNode(S, node)
            newValues.append(node.left.val)
            if node.right:
                newValues.append(node.right.val)
        values = newValues
        steps -= 1
        if steps == 0:
            break
    return values

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines


def solve(file_name, steps):
    lines = getLines(file_name)
    S = {}
    P = []
    nums = lines[0].split(" ")
    for num in nums:
        n = int(num)
        S[n] = Node(n)
        P.append(n)

    for step in range(steps):
        values = list(S.values())
        for value in values:
            nodes = generateNextNode(S, value)
        #print("---------------")
    #for key, val in S.items():
        #print(key, type(key), val, val.left, val.right)


    atBlink = getAtSteps(S, P, steps)
    return len(atBlink)
    
if __name__ == "__main__":
    steps = 25
    count = solve("input_a.txt", steps)
    print(count)
