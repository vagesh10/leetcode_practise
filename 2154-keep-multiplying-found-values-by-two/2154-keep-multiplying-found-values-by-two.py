class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        nums=sorted(nums)

        for i in range(len(nums)):
            if(nums[i]==original):
                original=2*nums[i]
            else:
                original+=0 
        return original
            
        