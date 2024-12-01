        
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
            
    left = [int(i) for i in left]
    right = [int(i) for i in right]
    left.sort()
    right.sort()
    print(left)
    print(right)
        
    value = 0
    for l, r in zip(left, right):
        value += abs(l-r)        

    print(value)
