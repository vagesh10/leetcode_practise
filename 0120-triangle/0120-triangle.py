class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        n=len(triangle)
       
        prev=[0]*n
        

        for i in range(0,n):
            cur=[0]*n

            for j in range(i+1):
                if(i==0 and j==0):
                    cur[j]=triangle[i][j]
                elif(j==0):
                    cur[j]=triangle[i][j]+prev[j]
                elif(j==i):
                    cur[j]=triangle[i][j]+prev[j-1]
                else:
                    cur[j]=triangle[i][j]+min(prev[j],prev[j-1])
            prev=cur
        

        return min(prev)
            
           
            
           
        
        return s

               

        