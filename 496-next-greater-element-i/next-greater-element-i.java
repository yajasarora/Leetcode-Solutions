class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] greater=new int[10000];
        int[] res=new int[nums1.length];
        for (int i=nums2.length-1;i>=0;i--) {
            if(i==nums2.length-1) {
                greater[nums2[i]]=-1;
                continue;
            }
            int nxt=nums2[i+1];
            while(nums2[i]>nxt && nxt!=-1) {       
                nxt=greater[nxt];
            }
            greater[nums2[i]]=nxt;
        }
        for (int i=0;i<nums1.length;i++) {
            res[i]=greater[nums1[i]];
        }
        return res;
    }
}

/*class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] nextGreaterArr = new int[10000];
        for (int j = nums2.length - 1; j >= 0; j--) {
            if(j == nums2.length - 1) {
                nextGreaterArr[nums2[j]] = -1;
                continue;
            }

            int ele = nums2[j + 1];
            while (nums2[j] > ele && ele != -1){
                ele = nextGreaterArr[ele];
            }
            nextGreaterArr[nums2[j]] = ele;
        }
        int[] res = new int[nums1.length];
        for (int j = 0; j < nums1.length; j++) {
            res[j] = nextGreaterArr[nums1[j]];
        }

        return res;
    }

} */