import re

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def solve(file_name):
    lines = getLines(file_name)

    mapping = {}
    for line in lines:
        c = line.split('-')
        c0 = c[0]
        c1 = c[1]
        if c0 in mapping:
            mapping[c0].append(c1)
        else:
            mapping[c0] = [c1]
        if c1 in mapping:
            mapping[c1].append(c0)
        else:
            mapping[c1] = [c0]

    s = set()
    for key, values in mapping.items():
        print('----------------------------------------------')
        print(f'{key}, {values}')
        for v1 in values:
            if v1 != key:
                v2s = mapping[v1]
                for v2 in v2s:
                    if v2 != key and v2 != v1 and v2 in values:
                        print(f'{key}, {values}, ({v1} != {v2}), {mapping[v1]=}')
                        it = tuple(sorted([key, v1, v2]))
                        it = tuple(sorted([key, v1, v2]))
                        s.add(it)

    lans = list(s)
    #print(lans)
    if False:
        tmp = [ 'aq,cg,yn', 'aq,vc,wq', 'co,de,ka', 'co,de,ta', 'co,ka,ta', 'de,ka,ta', 'kh,qp,ub', 'qp,td,wh', 'tb,vc,wq', 'tc,td,wh', 'td,wh,yn', 'ub,vc,wq' ]
        print(tmp)

    #chiefLans = [l for l in lans if 't' in l]
    chiefLans = []
    for lan in lans:
        for c in lan:
            if c[0] == 't':
                chiefLans.append(lan)

    for cl in chiefLans:
        print(cl)
    cl = set([''.join(x) for x in chiefLans])
    return len(cl)

if __name__ == "__main__":
    data = solve("input_a.txt")
    print(data)

    
