# Original solution:
# Uses a list for membership checks.
# `i not in nums` performs a linear search (O(n)) each iteration.
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing_numbers=[]

        max_val=max(nums)
        min_val=min(nums)


        for i in range(min_val, max_val):
            if i not in nums:
                missing_numbers.append(i)

        return missing_numbers

# Improved solution:
# Converts the list to a set so membership checks are O(1) on average
# instead of O(n). This reduces the overall time complexity from
# O(r * n) to O(n + r), where r is the size of the range.
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing_numbers=[]
        nums_set=set(nums)

        max_val=max(nums)
        min_val=min(nums)


        for i in range(min_val, max_val):
            if i not in nums_set:
                missing_numbers.append(i)

        return missing_numbers