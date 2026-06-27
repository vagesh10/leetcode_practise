class Solution:
    def countBits(self, n: int) -> List[int]:

        l=[]

        for i in range(0,n+1):
            rem=bin(i)
            l.append(rem.count('1'))
        return l


        