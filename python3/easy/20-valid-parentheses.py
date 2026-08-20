class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2!=0) or s[0]==']' or s[0]=='}' or s[0]==')':
            return False

        brackets={
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack=[]
        for char in s:
            if char in "({[":
                stack.append(char)

            elif char in ")}]" and stack and stack[-1]==brackets[char]:
                stack.pop()
            
            else: return False

        return not stack