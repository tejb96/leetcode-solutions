class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        write=1
        read=1

        while read < len(nums):

            if nums[read-1]==nums[read]:
                read+=1

            elif nums[read-1]!=nums[read]:
                nums[write]=nums[read]
                write+=1
                read+=1

        return write


