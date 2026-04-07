class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {

        int i=0;
        int j=0;
        int c=0;
        int n=nums.size();

        while(j<n){
            if(nums[j]==0){
                c++;
            }
            if(c>k){
                if(nums[i]==0)
                  c--;
                   i++;
            }
             j++;
        }
      return j-i;
        
    }
};