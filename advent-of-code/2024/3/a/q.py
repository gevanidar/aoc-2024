import re

def read_file(file_name):
    lines = []
    with open(file_name, 'r') as data:
        lines = data.readlines()
    return lines

    
def process_lines(lines):
    regex = r'mul\(\d{1,3}\,\d{1,3}\)'
    p = re.compile(regex)
    matches = p.findall(line)
    return matches

def find_products(processed_line):
    products = []
    for match in processed_line:
        regex = r'\d+'
        p = re.compile(regex)
        digits = p.findall(match)
        product = int(digits[0]) * int(digits[1])
        products.append(product)
    return products
        
if __name__ == "__main__":
    file_name = 'data_test.txt'
    file_name = 'data_real.txt'
    lines = read_file(file_name)


    total_value = 0
    for line in lines:
        processed_line = process_lines(line)
        products = find_products(processed_line)
        line_value = sum(products)
        total_value += line_value

    print(total_value)


