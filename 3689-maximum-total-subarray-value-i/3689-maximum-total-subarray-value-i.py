class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        minValue=nums[0]
        maxValue=nums[0]
        n=len(nums)


        for i in range(0,n):
           
            if(nums[i]<minValue):
                minValue=nums[i]
        

        for i in range(0,n):
           
            if(nums[i]>maxValue):
                maxValue=nums[i]
        

        return (maxValue-minValue)*k






        