from typing import List
import math

class Solution:
    def reverse(self, x: int) -> int:
        stringVal = str(x)
        stringVal = stringVal.split(".")[0]
        negative = stringVal[0] == "-"
        if negative:
            stringVal = stringVal.split("-")[1][::-1]
        else:
            stringVal = stringVal[::-1]

        newVal = 0
        power = math.pow(10, len(stringVal)-1)
        for s in stringVal:
            val = int(s)
            newVal += val * power
            power /= 10

        if newVal < - math.pow(2, 31) or newVal >= math.pow(2,31):
            return 0
            
        return -int(newVal) if negative else int(newVal)
