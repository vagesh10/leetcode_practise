class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(n-1,-1,-1):
            val=nums[i]
            while(val>0):
                ans.append(val%10)
                val//=10
        ans.reverse()
        return ans

        