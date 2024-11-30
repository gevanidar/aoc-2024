from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = []
        max_length = 0
        for char in s:
            
            if char in ss:
                length = len(ss) 
                if length > max_length:
                   max_length = length
                index = ss.index(char)
                if length > 1:
                    ss = ss[index+1:]
                    ss.append(char)
            else:
                ss.append(char)
        if max_length < len(ss):
            max_length = len(ss)
        return max_length
                
