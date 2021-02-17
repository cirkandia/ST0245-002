
class Taller04{
 
    public static int arrayMax(int[] array, int n) {
        int max, temp;
        max = array[n];
        if(n != 0) {
            temp = arrayMax(array, n-1); 
            if(temp >= max)
                max = temp;
            }
            return max;
    }
 
 
 
    public static boolean groupSum(int start, int[] nums, int target) {
        if (start == nums.length) 
            return target == 0; 
        else
            return groupSum(start+1, nums, target) 
            || groupSum(start+1,nums,target-nums[start]);
 
    }
 
    public static long fibonacci(int n) {
        if (n <= 1) {
            return n;
        } else {
            return fibonacci(n - 1) + fibonacci(n - 2); 
        }
    }
}
