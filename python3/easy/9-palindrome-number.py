class Solution:
    def isPalindrome(self, x: int) -> bool:
        text=str(x)
        right=len(text)-1
        left=0

        while left < right:
            if(text[left]!=text[right]):
                return False

            left+=1
            right-=1

        return True


# Solved without converting x to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=x
        reverse_number=0

        while original>0:
            digit=original%10
            original=original//10
            reverse_number=reverse_number*10+digit


        return x==reverse_number


            

            