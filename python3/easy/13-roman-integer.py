# Original solution
# Complexity: O(n) time and O(1) space
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        num=0

        for index, c in enumerate(s):
            if index<len(s)-1 and (roman_int[c]>=roman_int[s[index+1]]):
                num=num+roman_int[c]
            elif index<len(s)-1 and roman_int[c]<roman_int[s[index+1]]:
                num-=roman_int[c]
            else:
                num+=roman_int[c]

        return num

# Improved solution
# Complexity: O(n) time | O(1) space
#
# Improvements:
# - Initializes the total with the last Roman numeral, eliminating the need
#   for a special-case check inside the loop.
# - Iterates only through the remaining characters, simplifying the logic.
# - Reduces conditional branching, making the code cleaner and slightly
#   more efficient while maintaining the same time and space complexity.
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        num=roman_int[s[-1]]

        for i in range(len(s)-1):
            if roman_int[s[i]]<roman_int[s[i+1]]:
                num-=roman_int[s[i]]                
            else:
                num+=roman_int[s[i]]

        return num