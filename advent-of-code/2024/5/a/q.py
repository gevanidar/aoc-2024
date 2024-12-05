import re

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def checkCommandObeysRules(command, rules):
    seen = set()
    for c in command:
        if c in rules:
            for r in rules[c]:
                if r in seen:
                    #print(f'{rules[r]=}')
                    return False
        seen.add(c)
            
    return True

def process_lines(lines):
    processing_rules = True
    rules = {}
    commands = [ ]
    for line in lines:
        #print(f'{line=} {not line=}')
        if not line:
            processing_rules = False
        elif processing_rules:
            x,y = line.split("|")
            if x in rules:
                rules[x].append(y)
            else:
                rules[x] = [y]
        else:
            commands.append(line.split(','))
    return rules, commands

def solve(file_name):
    lines = getLines(file_name)
    rules, commands = process_lines(lines)

    numbers = [ ] 
    for command in commands:
        if (checkCommandObeysRules(command, rules)):
            numbers.append(int(command[len(command) // 2]))

    #print(f'{rules=}')
    #print(f'{commands=}')
    return sum(numbers)

if __name__ == "__main__":
    count = solve("data_real.txt")
    print(count)
