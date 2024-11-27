import math

def remainder_floor(divident, divisor):
    return math.floor(divident / divisor)


if __name__ == "__main__":
    divident = 1000
    divident -= 1
    times_3 = remainder_floor(divident, 3)
    times_5 = remainder_floor(divident, 5)
    times_15 = remainder_floor(divident, 15)

    mean_3 = 3 * (times_3 + 1) / 2
    mean_5 = 5 * (times_5 + 1) / 2
    mean_15 = 15 * (times_15 + 1) / 2
    print(times_3, mean_3, times_5, mean_5, times_15, mean_15)

    value = times_3 * mean_3 + times_5 * mean_5 - times_15 * mean_15
    print(value)
