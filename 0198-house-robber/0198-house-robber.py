class Solution:
    def rob(self, nums: List[int]) -> int:

        p2=nums[0]
        n=len(nums)

        if n==1:
            return p2
        
        p1=max(nums[0],nums[1])

        n=len(nums)

        for i in range(2,n):

            pick=nums[i]+p2
            not_pick=p1
            curr = max(pick,not_pick)

            p2=p1
            p1=curr

        return p1
        