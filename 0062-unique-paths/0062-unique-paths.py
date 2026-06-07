class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prior=[1]*n
       

        for i in range(1,m):
            cur=[1]*n
            for j in range(1,n):
                cur[j]=cur[j-1]+prior[j]
            
            prior=cur
            

           

        return prior[n-1]
        