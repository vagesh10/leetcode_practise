class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])
        prev=[0]*n
        cur=[0]*n

        for i in range(0,m):
            for j in range(0,n):
                if(grid[i][j]==1):
                    cur[j]=0
                
                elif(i==0 and j==0):
                    cur[j]=1
                else:
                    right=0
                    down=0

                    if(i>0):
                        down=prev[j]
                    if(j>0):
                        right=cur[j-1]
                    cur[j]=right+down
                
            prev=cur
        return cur[n-1]
        