        
if __name__ == "__main__":
    test_file_name = 'data_test.txt'
    test_file_name = 'data_real.txt'
    right = []
    left = []
    with open(test_file_name, 'r') as test_data:
        line = test_data.readline()
        while line:
            line = line.strip('\n')
            line = line.split(" ")
            left.append(line[0])
            right.append(line[-1])
            #print(line)

            line = test_data.readline()
            
    left_set = {}
    for val in left:
        val = int(val)
        if val in left_set:
            left_set[val] = left_set[val] + 1
        else:
            left_set[val] = 1

    right_set = {}
    for val in right:
        val = int(val)
        if val in right_set:
            right_set[val] = right_set[val] + 1
        else:
            right_set[val] = 1
            
    print(left_set)
    print(right_set)

    total = 0
    for key, val in left_set.items():
        if key in right_set:
            total += key * val * right_set[key]
    print(total)

