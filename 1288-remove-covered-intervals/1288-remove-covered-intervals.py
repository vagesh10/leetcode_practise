class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:


        s=sorted(intervals,key=lambda x:(x[0],-x[1]))
        
        n=len(intervals)
        
        c=0
        max_end=0

        for i,j in s:
            if(j<=max_end):
                c+=1
            else:
                max_end=j
            


        return n-c

    
        