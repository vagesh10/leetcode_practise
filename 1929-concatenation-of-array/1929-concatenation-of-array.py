class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        
        l=len(nums)
        ans=[]

        for i in range(l):
            ans.append(nums[i])

        for j in range(l,(2*l)):
            ans.append(nums[j-l])
        
        return ans

        