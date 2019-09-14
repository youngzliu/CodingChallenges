public class Solution {
    public int ClimbStairs(int n) {
        if(n == 1){
            return 1;
        }
        else if(n == 2){
            return 2;
        }
        else{
            int[] results = new int[n+1];
            results[1] = 1;
            results[2] = 2;
            for(int i = 3; i <= n; i++){
                FindStairs(i, results);
            }
            return results[n];
        }
    }
    
    public void FindStairs(int n, int[] results){
        results[n] = results[n-1] + results[n-2];
    }
}