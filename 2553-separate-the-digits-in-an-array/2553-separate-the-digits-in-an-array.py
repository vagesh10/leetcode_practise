class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        for i in range(0,n):
            s=str(nums[i])
            for i in s:
                l=int(i)
                ans.append(l)

           
                
        
                
        return ans

        