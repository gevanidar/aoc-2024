import re
from itertools import product


def getLines(file_name):
    lines = []
    with open(file_name, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    return lines

def process_lines(lines):
    answers = []
    equations = []
    for line in lines:
        y, xs = line.split(":")
        answers.append(int(y.strip()))
        equation = []
        xs = xs.split(" ")
        for x in xs:
            if x:
                equation.append(int(x))
        equations.append(equation)

    return answers, equations




def checkValid(answer, equation, muls):
    #print(equation, muls)
    for mul in muls:
        val = equation[0]
        tmp = str(val)#print(val)
        for index, eq in enumerate(equation[1:]):
            if mul[index] == "*":
                val *= eq
                tmp += f'*{eq}'
            else:
                val += eq
                tmp += f'+{eq}'
        #print(f'{tmp=} ?= {answer=}, {val=}')
        if val == answer:
            return True

    return False


def solve(file_name):
    lines = getLines(file_name)
    answers, equations = process_lines(lines)

    total = 0
    for answer, equation in zip(answers, equations):
        #print('------------------------------------')
        operators = ["+", "*"]
        muls = [''.join(s) for s in product(operators, repeat=len(equation))]
        #print(muls)

        valid = checkValid(answer, equation, muls)
        if valid:
            #print(f'{answer}, {equation=}')
            total += answer

    return total

if __name__ == "__main__":
    count = solve("input_a.txt")
    print(count)
