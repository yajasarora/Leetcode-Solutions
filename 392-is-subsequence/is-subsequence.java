class Solution {
    public boolean isSubsequence(String s, String t) {
        char[] ss=s.toCharArray();
        char[] tt=t.toCharArray();
        if (ss.length<1) {
            return true;
        }
        if (ss.length<=tt.length) {
            int j=0;
            for (int i=0;i<tt.length;i++) {
                if (tt[i]==ss[j]) {
                    j++;
                }
                if (j==ss.length) {
                    return true;
                }
            }


        }
    return false;
}}