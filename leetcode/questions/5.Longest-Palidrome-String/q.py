from typing import List

def getPalindrome(s, left, right):
    if left == right:
        return getPalindrome(s, left - 1, right + 1)
    elif left < 0 or len(s) <= right:
        # Return previous
        left += 1
        right -= 1
        return {'left': left, "right": right, 'length': right - left}
    elif s[left] != s[right]:
        if right - left == 1:
            # Example: "ab"
            return {'left': -1, "right": -1, 'length': 0}
        # Return previous
        left = left + 1
        right = right - 1
        return {'left': left, "right": right, 'length': right - left}
    else:
        return getPalindrome(s, left - 1, right + 1)
    
def getPalindromeInDirection(s, left, right, direction):
    longest_palindrome =  {'left': -1, "right": -1, 'length': -1}
    if direction < 1:
        end = left + 1
        for index in range(0, end):
            left_index = left - index
            right_index = right - index
            palindrome = getPalindrome(s, left_index, right_index)
            length = palindrome['right'] - palindrome['left']
            if longest_palindrome['length'] < length:
                longest_palindrome = palindrome
    else:
        end = len(s) - right
        for index in range(0, end):
            left_index = left + index
            right_index = right + index
            palindrome = getPalindrome(s, left_index, right_index)
            length = palindrome['right'] - palindrome['left']
            if longest_palindrome['length'] < length:
                longest_palindrome = palindrome
    return longest_palindrome


class Solution:
    def longestPalindrome(self, s: str) -> str:
            
        length = len(s)
        if length <= 1:
            return s

        mid = length // 2

        # To the left
        palindrome_left_1 = getPalindromeInDirection(s, mid, mid, - 1) # From double
        longest_palindrome = palindrome_left_1 
        palindrome_left_2 = getPalindromeInDirection(s, mid - 1, mid, - 1) # From single
        if longest_palindrome['length'] < palindrome_left_2['length']:
            longest_palindrome = palindrome_left_2
        # To the right
        palindrome_right_1 = getPalindromeInDirection(s, mid, mid, + 1) # From single
        if longest_palindrome['length'] < palindrome_right_1['length']:
            longest_palindrome = palindrome_right_1
        palindrome_right_2 = getPalindromeInDirection(s, mid, mid + 1, 1) # From double
        if longest_palindrome['length'] < palindrome_right_2['length']:
            longest_palindrome = palindrome_right_2

        return s[longest_palindrome['left']:longest_palindrome['right']+1]

