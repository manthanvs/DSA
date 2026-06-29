class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for(String o : operations){
            if(o.charAt(1)=='-')
                x--;
            else{
                x++;
            }
        }
        return x;
    }
}