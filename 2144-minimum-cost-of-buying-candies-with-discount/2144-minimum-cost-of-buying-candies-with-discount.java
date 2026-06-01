class Solution {
    public int minimumCost(int[] cost) {
        if(cost.length==1){
            return cost[0];
        }
        Arrays.sort(cost);
        int i=cost.length-1;
        int sum=0;
        while(i>=0){
            if(i-1>=0){
            sum+=cost[i]+cost[i-1];
            }
            else{
                sum+=cost[i];

            }
            i-=3;
        }
        return sum;
        
    }
}