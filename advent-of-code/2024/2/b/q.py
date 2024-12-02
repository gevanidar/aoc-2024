def inRange(diff):
    return 1 <= diff and diff <= 3

def checkIfGradually(values):
    diffs = []
    last = values[0]
    for val in values[1:]:
        next = int(val)

        diff = next - last
        
        diffs.append(diff)

        #print(f'{diff=} = {next=} - {last=}')

        last = next

    if diffs[0] < 0:
        diffs = [-i for i in diffs]
    #print(values, diffs)

    minimum = min(diffs)
    maximum = max(diffs)
    return 1 <= minimum and maximum <= 3

def process_line(line):
    values = [int(i) for i in line if len(i) >= 1]
    last = values[0]

    index = -1
    direction = 0
    for i, val in enumerate(values[1:]):
        diff = val - last
        if diff * diff > 9 or diff * diff < 1:
            index = i
            break
        current_direction = -1 if diff < 0 else 1
        if direction == 0:
            direction = current_direction
        elif direction != current_direction:
            index = i
            break
        last = val

    if index == -1:
        return checkIfGradually(values)
    elif index == 0:
        second = [v for i, v in enumerate(values) if i != 1]
        return checkIfGradually(values[1:]) or checkIfGradually(second)
    elif index == len(values) - 2:
        second = [v for i, v in enumerate(values) if i != index - 1]
        #print(f'{checkIfGradually(values[:-1])=} {values[:-1]=} or {checkIfGradually(second)=} {second=}')
        return checkIfGradually(values[:-1]) or checkIfGradually(second)
    else:
        first = [v for i, v in enumerate(values) if i != index - 1]
        second = [v for i, v in enumerate(values) if i != index]
        third = [v for i, v in enumerate(values) if i != index + 1]
        return checkIfGradually(first) or checkIfGradually(second) or checkIfGradually(third)


if __name__ == "__main__":
    test_file_name = 'data_test.txt'
    #test_file_name = 'data_test_2.txt'
    test_file_name = 'data_real.txt'
    with open(test_file_name, 'r') as test_data:
        line = test_data.readline()

        safe = 0
        while line:
            print(line)
            line = line.strip('\n').split(" ")
            if process_line(line):
                print('-----------ABOVE')
                safe += 1
            line = test_data.readline()
        print(f'{safe=}')


