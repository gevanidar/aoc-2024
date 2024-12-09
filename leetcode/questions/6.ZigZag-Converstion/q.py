from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lines = [[] for i in range(numRows)]
        row = 0
        direction = 1
        maxRowIndex = numRows - 1
        for char in s:
            lines[row].append(char)
            row += direction
            if row == 0:
                direction = 1
            elif row == maxRowIndex:
                direction = -1

        text = ""
        for row in lines:
            text += ''.join(row)

        return text
        
