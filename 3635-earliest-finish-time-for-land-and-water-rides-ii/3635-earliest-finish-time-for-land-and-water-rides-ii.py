class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:


        lTime=len(landStartTime)
        wTime=len(waterStartTime)

        l=w=minL=minW=float('inf')
        

        for i in range(lTime):
            l=min(l,landStartTime[i]+landDuration[i])
                
        for j in range(wTime):
                w=min(w,waterStartTime[j]+waterDuration[j])
                minL=min(minL,max(waterStartTime[j],l)+waterDuration[j])

        for k in range(lTime):
            minW=min(minW,max(landStartTime[k],w)+landDuration[k])

                
        

        return min(minW,minL)
        