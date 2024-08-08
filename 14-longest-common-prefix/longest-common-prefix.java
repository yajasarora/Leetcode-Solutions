class Solution {
    public String longestCommonPrefix(String[] strs) {
       Arrays.sort(strs);
       String s1=strs[0];
       String s2=strs[strs.length-1];
       int j=0;
       while (j<s1.length() && j<s2.length()) {
           if(s1.charAt(j)==s2.charAt(j)) {
               j++;

           }
           else {
               break;
           }
       }
    return strs[0].substring(0,j);
    }
}