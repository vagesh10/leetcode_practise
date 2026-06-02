class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:


        t1=0
        
        Ltime=len(landStartTime)
        Wtime=len(waterStartTime)
        ans=float('inf')

        for i in range(0,Ltime):
            for j in range(0,Wtime):

                Land=landStartTime[i]+landDuration[i]
                LandTime=max(Land,waterStartTime[j])+waterDuration[j]
                ans=min(ans,LandTime)

                Water=waterStartTime[j]+waterDuration[j]
                WaterTime=max(Water,landStartTime[i])+landDuration[i]
                ans=min(ans,WaterTime)
        return ans

        

                


        
                


        

        