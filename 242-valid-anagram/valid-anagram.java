class Solution {
    public boolean isAnagram(String s, String t) {
    
        char[] ch=s.toCharArray();
        char[] th=t.toCharArray();
        Arrays.sort(ch);
        Arrays.sort(th);
           if(Arrays.equals(ch,th)) {
               return true;
           }
            
        else {
            return false;
        }
    }
}