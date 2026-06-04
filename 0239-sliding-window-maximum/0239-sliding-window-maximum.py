class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        dq=deque()

        i=0
        n=len(nums)

        while i<n:

            if(len(dq)!=0 and i>=k and dq[0] ==nums[i-k]):
                dq.popleft()

            
            while len(dq) !=0 and dq[-1] < nums[i]:
                dq.pop()

            dq.append(nums[i])

            if i>=k-1:
                res.append(dq[0])
            i+=1
        return res

        