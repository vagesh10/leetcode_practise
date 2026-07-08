class Solution:
    def subsetSum(self,n,k,arr):

        prev=[0]*(k+1)
        prev[0]=1

        for i in range(n):
            cur=[0]*(k+1)
            cur[0]=1

            for j in range(1,k+1):
                notPick=prev[j]
                pick=0

                if(arr[i]<=j):
                    pick=prev[j-arr[i]]
                cur[j]=pick or notPick
            prev=cur[:]
        if(prev[k]==1):
            return True
        else:
            return False

    def canPartition(self, nums: List[int]) -> bool:

        n=len(nums)
        s=sum(nums)

        if(s%2==1):
            return False
        
        return self.subsetSum(n,s//2,nums)

    


        