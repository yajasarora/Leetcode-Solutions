class Solution {
    public int pivotIndex(int[] nums) {
        int total=0;
        int leftsum=0;
        for (int i: nums) {
            total+=i;
        }
        for (int i=0;i<nums.length;i++) {
            //int rightsum=total-nums[i]-leftsum;
            if (leftsum*2==total-nums[i]) {
                return i;
            }
            leftsum+=nums[i];
        }
        return -1;
    }
}