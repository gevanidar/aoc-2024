        
if __name__ == "__main__":
    test_file_name = 'data_test.txt'
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
            #print(diffs)
            is_safe = True
            for diff in diffs:
                if 1 <= diff and diff <= 3:
                    continue
                else:
                    is_safe = False
                    break
            #print(is_safe)
            if is_safe:
                safe += 1

            line = test_data.readline()
        print(safe)
