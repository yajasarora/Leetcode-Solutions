class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> ans=new HashMap<>();
        for (String i: strs) {
            char[] temp=i.toCharArray();
            Arrays.sort(temp);
            String sortedword= new String(temp);

            if (!ans.containsKey(sortedword)) {
                ans.put(sortedword, new ArrayList<>());
            }

            ans.get(sortedword).add(i);
        } 

        return new ArrayList<>(ans.values());
    }
}