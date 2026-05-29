class Solution:
    def minElement(self, nums: List[int]) -> int:

        s=0
        n=len(nums)
        ans=[]

        for i in nums:
            while(i!=0):
                rem=i%10
                s+=rem
                
                i//=10
            ans.append(s)
            s=0
           

        return min(ans)
        

        