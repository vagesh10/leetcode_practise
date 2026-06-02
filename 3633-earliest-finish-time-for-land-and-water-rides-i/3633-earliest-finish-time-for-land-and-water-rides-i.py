class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        ans=float('inf')

        lTime=len(landStartTime)
        wTime=len(waterStartTime)

        for i in range(lTime):
            for j in range(wTime):

                land=landStartTime[i]+landDuration[i]
                landTime=max(land,waterStartTime[j])+waterDuration[j]
                ans=min(ans,landTime)

                water=waterStartTime[j]+waterDuration[j]
                waterTime=max(water,landStartTime[i])+landDuration[i]
                ans=min(ans,waterTime)
        return ans
        