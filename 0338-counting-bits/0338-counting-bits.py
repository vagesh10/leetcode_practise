class Solution:
    def countBits(self, n: int) -> List[int]:

        l=[]

        for i in range(0,n+1):
            rem=i.bit_count()
            l.append(rem)
        return l


        