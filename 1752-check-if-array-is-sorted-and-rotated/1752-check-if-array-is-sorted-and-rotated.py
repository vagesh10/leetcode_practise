class Solution:
    def check(self, nums: List[int]) -> bool:

        b=len(nums)
        c=0

        for i in range(b):
            if (nums[i] > nums[(i+1)%b]):
                c+=1
        

        return c<=1
        