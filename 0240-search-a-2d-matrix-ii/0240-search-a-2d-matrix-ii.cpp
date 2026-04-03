class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int rSize=matrix.size();
        int cSize=matrix[0].size();

        int row=0;
        int col=cSize-1;

        while(row < rSize && col>=0){
            int curr=matrix[row][col];

            if(curr==target){
                return true;
            }
            else if(curr > target){
                col-=1;
            }
            else{
                row+=1;
            }
        }

        return false;
        
    }
};