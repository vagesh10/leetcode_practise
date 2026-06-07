class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prior=[1]*n
        cur=[0]*n

        cur[0]=1 

        for i in range(1,m):
            for j in range(1,n):
                cur[j]=cur[j-1]+prior[j]
            

            for k in range(1,n):
                prior[k]=cur[k]
        

        return prior[n-1]
        