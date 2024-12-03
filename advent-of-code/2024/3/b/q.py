import re

def read_file(file_name):
    lines = []
    with open(file_name, 'r') as data:
        lines = data.read()
    return lines
   
        
if __name__ == "__main__":
    file_name = 'data_test.txt'
    file_name = 'data_real.txt'
    data = read_file(file_name)

    total = 0
    #print('---New line---')
    regex = r'mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don\'t\(\)'
    p = re.compile(regex)
    matches = p.findall("do()" + data)

    do = False
    value = 0
    p = re.compile(r'\d+')
    for match in matches:
        #print(f'{match=}')
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        elif do:
            factors = p.findall(match)
            product = int(factors[0]) * int(factors[1])
            value += product
    total += value

    print(total)
