class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for(int i:nums) {
            nums[Math.abs(i)-1]=-1*Math.abs(nums[Math.abs(i)-1]);
        }
        List<Integer> ans=new ArrayList<>();
        for(int i=0;i<nums.length;i++) {
            if (nums[i]>0) {
                ans.add(i+1);
            }
        }
        return ans;
    }
}