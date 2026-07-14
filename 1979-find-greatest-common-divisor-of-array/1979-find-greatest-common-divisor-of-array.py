class Solution:
    def findGCD(self, nums: List[int]) -> int:


        s=min(nums)
        m=max(nums)
        res=1
        
       

        for i in range(2,s+1):
        
            if(s%i==0 and m%i==0):
                res=i

                
        return res

