class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m=len(grid)
        n=len(grid[0])
        cur=[0]*n
        prev=[0]*n

        for i in range(0,m):
            for j in range(0,n):
                if(i<0 or j<0):
                    return float('inf')
                if(i==0 and j==0):
                    cur[j]=grid[0][0]
                

                else:
                    right=float('inf')
                    down=float('inf')

                    if(i>0):
                        down=prev[j]
                    if(j>0):
                        right=cur[j-1]
                    
                    cur[j]=grid[i][j]+min(right,down)
            prev=cur
        
        return cur[n-1]
        

        