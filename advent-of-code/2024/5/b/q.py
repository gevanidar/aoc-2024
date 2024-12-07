import re

def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

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

def makeSureCommandObeysRules(command, rules):
    seen = set()
    new_command = []
    #print(f'{rules=}')
    for c in command:
        #print(f'{new_command=}, {c=}')
        if c in rules:
            index = len(command)
            for r in rules[c]:
                if r in seen:
                    new_index = new_command.index(r) if r in new_command else index 
                    #print(c, r, index, new_index)
                    if new_index < index:
                        index = new_index
            if index < len(command):
                new_command.insert(index, c)
            else:
                new_command.append(c)
        else:
            new_command.append(c)
        seen.add(c)
            
    return new_command

def solve(file_name):
    lines = getLines(file_name)
    rules, commands = process_lines(lines)

    numbers = [ ] 
    for command in commands:
        if not (checkCommandObeysRules(command, rules)):
            #print(command)
            command = makeSureCommandObeysRules(command, rules)
            #print(command)
            numbers.append(int(command[len(command) // 2]))

    #print(f'{rules=}')
    #print(f'{commands=}')
    return sum(numbers)

if __name__ == "__main__":
    count = solve("data_real.txt")
    print(count)
