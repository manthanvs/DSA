class Solution {
    public int[][] transpose(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int transposematrix[][] = new int[cols][rows];

        for(int i = 0 ; i < matrix[0].length ; i++){
            for(int j = 0 ; j < matrix.length ; j++){
                transposematrix[i][j] = matrix[j][i];
            }
        }
        return transposematrix;
    }
}