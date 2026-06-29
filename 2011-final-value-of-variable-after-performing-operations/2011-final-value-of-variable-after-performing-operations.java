class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for(String o : operations){
            System.out.println(o.charAt(1));
            if(o.charAt(1)=='-')
                x--;
            else{
                x++;
            }
        }
        return x;
}