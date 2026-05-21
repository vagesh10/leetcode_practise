class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        s=set()
        maxi=0

        for num in arr1:
            while num >0:
                s.add(num)
                num//=10
        print(s)
        

        for num in arr2:
            while num > 0:
                if num in s:
                     maxi=max(maxi,len(str(num)))
                     break
                num//=10
        

        return maxi


        