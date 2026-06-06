class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        totalSum=0
        n=len(nums)
        ans=[]

        for i in range(0,n):
            totalSum+=nums[i]

        

        left=0

        for i in range(0,n):
            right=totalSum-nums[i]-left
            ans.append(abs(left-right))
            left+=nums[i]
        

        return ans


        