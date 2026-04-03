class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int rSize=matrix.size();
        int cSize=matrix[0].size();

        int row=0;
        int col=cSize-1;

        while(row < rSize && col >=0){
            int curr=matrix[row][col];

            if(target==curr){
                return true;
            }
            else if(target > curr){
                row++;
            }
            else{
                col--;
            }
        }

        return false;
        
    }
};