class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        n=len(nums)

        diff=[0] * (2*limit+2)

        for i in range(n//2):
            a=nums[i]
            b=nums[n-1-i]


            low=1+min(a,b)
            high=limit+max(a,b)
            pair_sum=a+b 

            diff[2]+=2
            diff[2*limit+1]-=2

            diff[low]-=1
            diff[high+1]+=1

            diff[pair_sum]-=1
            diff[pair_sum+1]+=1
        ans=float('inf')
        cur=0
        for s in range(2,2*limit+1):
            cur+=diff[s]
            ans=min(ans,cur)

        return ans
