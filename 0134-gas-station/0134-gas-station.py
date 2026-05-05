class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if(sum(gas) < sum(cost)):
            return -1

        n=len(gas)
        start=0
        cur=0

        for i in range(n):
            cur+=gas[i]-cost[i]

            if cur <0:
                start=i+1
                cur=0
        return start
        