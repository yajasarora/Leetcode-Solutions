class Solution {
    public int longestValidParentheses(String s) {
        Stack<Character> ch = new Stack<>();
                Stack<Integer> ind = new Stack<>();
                        ind.push(-1);
                                int ans = 0;

                                        for(int i = 0; i < s.length(); i++) {
                                                    if(s.charAt(i) == '(') {
                                                                    ch.push('(');
                                                                                    ind.push(i);
                                                                                                } else {
                                                                                                                if(!ch.isEmpty() && ch.peek() == '(') {
                                                                                                                                    ch.pop();
                                                                                                                                                        ind.pop();
                                                                                                                                                                            ans = Math.max(ans, (i - ind.peek()));
                                                                                                                                                                                            } else {
                                                                                                                                                                                                                ind.push(i);
                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                    }

                                                                                                                                                                                                                                                            return ans;
    }
}
