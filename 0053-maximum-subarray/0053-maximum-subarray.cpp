class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        int n=nums.size();

        int sum=0,maxSum=nums[0];

        for(int i=0;i<n;i++){
            if(sum+nums[i]<nums[i]){
                sum=nums[i];
            }
            else{
                sum+=nums[i];
            }

            if(sum>maxSum){
                maxSum=sum;
            }
        }

        return maxSum;
        
    }
};