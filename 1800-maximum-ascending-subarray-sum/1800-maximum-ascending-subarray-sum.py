class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:


        s=nums[0]
        maxSum=nums[0]
        n=len(nums)
       

        for i in range(1,n):
            if(nums[i]>nums[i-1]):
                s+=nums[i]
                print(nums[i])
            else:
                maxSum=max(maxSum,s)
                s=nums[i]
        maxSum=max(maxSum,s)
       

               
        
        return maxSum
        