class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length()!=t.length()) {
            return false;
        }
        Map<Character,Integer> mapts=new HashMap<Character,Integer>();
        Map<Character,Integer> mapst=new HashMap<Character,Integer>();
        for (int i=0; i<s.length();i++) {
            char c=s.charAt(i);
            char d=t.charAt(i);
            if (mapst.containsKey(c) || mapts.containsKey(d)) {
            if(mapst.get(c)!=mapts.get(d)) {
                return false;
            }
            }
            else {
            mapst.put(c,i);
            mapts.put(d,i);
            }
        }
        return true;
    }

}