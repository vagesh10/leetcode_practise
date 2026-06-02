class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        p1=nums[0]
        if(n==1):
            return p1

        p2=max(nums[0],nums[1])

        for i in range(2,n):
            pick=nums[i]+p1
            not_pick=p2

            curr=max(pick,not_pick)

            p1=p2
            p2=curr
            

        return p2


            

            


        