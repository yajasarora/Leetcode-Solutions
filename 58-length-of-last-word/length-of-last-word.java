class Solution {
    public int lengthOfLastWord(String s) {
        int j=0;
        char[] ss=s.toCharArray();
        for (int i=ss.length-1;i>=0;i--) {
                if (ss[i]==' ') {
                    continue;
                }
                while (ss[i]!=' ') {
                    j++;
                    i--; 
                    if (i==-1) {
                        break;
                    }
                }
                if(j>0) {
                    break;
                }
        }
        return j;
    }
}