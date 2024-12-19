import re
from itertools import permutations

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def solve(file_name):
    lines = getLines(file_name)
    patterns = lines[0].split(", ")


    designs = lines[2:]

    count = 0
    for design in designs:
        pat = []
        for pattern in patterns:
            if pattern in design:
                pat.append(pattern)


        print(design)
        if f(design, pat):
            print("Design is in")
            count+=1
        else:
            print("design is not in")
        #print("######")

    return count

def f(design, patterns):
	if len(design) == 0:
		return True
	for pattern in patterns:
		length = len(pattern)
		if length > len(design):
			continue
		if design[:length] == pattern:
			val = f(design[len(pattern):], patterns)
			if val:
			    return True
	return False

    
if __name__ == "__main__":
    data = solve("input_a.txt")
    print(data)
    # too low 234
