class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        
        if length==1 or k==length or (k>length and k%length==0):
            return

        nums.reverse()
        i=0
        j=k-1

        if k>length:
            floor_div=k//length
            j=k-(floor_div*length)-1

        while i<j:
            print(i,j)
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

        i=k
        j=length-1

        if k>length:
            floor_div=k//length
            i=k-(floor_div*length)

        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1         

