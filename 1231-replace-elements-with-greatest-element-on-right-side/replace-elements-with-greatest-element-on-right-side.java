class Solution {
    public int[] replaceElements(int[] arr) {
        int max=-1;
        int temp;
        for (int i=arr.length-1;i>=0;i--) {
            temp=arr[i];
            arr[i]=max;
            if (temp>max) {
                max=temp;
            }

        }
       //arr[arr.length-1]=-1;
        return arr;
    }
}