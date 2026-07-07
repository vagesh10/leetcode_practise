class Solution:
    def sumAndMultiply(self, n: int) -> int:

        s=str(n)
        l=[]

        for i in s:
            if i != '0':
                i=int(i)
                l.append(i)
        

        

        r=sum(l)

        res=("".join(map(str,l)))

        p=int(res) if res else 0

        return p*r

      

        