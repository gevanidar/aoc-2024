def inRange(diff):
    return 1 <= diff and diff <= 3

def checkIfSafe(diffs, index):
    new_diffs = [ ]
    if index == 0:
        new_diffs = diffs[1:]
    elif len(diffs) - 1 == index:
        new_diffs = diffs[:-1]
    else:
        # So this always shifts left
        new_diffs = diffs[:index]
        new_diffs[index-1] = new_diffs[index-1] + diffs[index]
        new_diffs.extend(diffs[index+1:])
        # Should contain shift right
    return 1 <= min(new_diffs) and max(new_diffs) <= 3

    return False

if __name__ == "__main__":
    test_file_name = 'data_test.txt'
    test_file_name = 'data_test_2.txt'
    test_file_name = 'data_real.txt'
    with open(test_file_name, 'r') as test_data:
        line = test_data.readline()

        safe = 0
        while line:
            line = line.strip('\n')
            line = line.split(" ")

            diffs = []
            last = int(line.pop(0))
            for val in line:
                if len(val) == 0:
                    continue
                next = int(val)

                diff = next - last
                    
                diffs.append(diff)

                last = next

            if diffs[0] < 0:
                diffs = [-i for i in diffs]

            is_safe = True
            problem_dampener_index = -1
            problem_dampener = 1
            for index, diff in enumerate(diffs):
                if inRange(diff):
                    continue
                else:
                    problem_dampener -= 1
                    problem_dampener_index = index
                    break
            if problem_dampener == 1:
                safe += 1
            elif problem_dampener == 0:
                if checkIfSafe(diffs, problem_dampener_index):
                    safe +=1
                

            line = test_data.readline()

        print(safe)
