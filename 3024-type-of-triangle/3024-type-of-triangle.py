class Solution:
    def triangleType(self, nums: List[int]) -> str:

        s1=nums[0]
        s2=nums[1]
        s3=nums[2]

        if(s1+s2 <= s3 or s2+s3 <= s1 or s1+s3 <=s2):
            return "none"


        if(s1==s2==s3):
            return "equilateral"
        elif(s1==s2 or s2==s3 or s3==s1):
            return "isosceles"
       
        else:
            return "scalene"
        