class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> set=new HashSet<String>();    
        for (String e : emails) {
            String temp=format(e);
            set.add(temp);
        }
    return set.size();

    }
    private String format(String email) {
        StringBuilder sb=new StringBuilder("");
        String domain="";
        int placeholder=0;
        for(int i=0;i<email.length();i++) {
            char c=email.charAt(i);
            if (c=='.') {
                continue;
            }
            if (c=='@' || c=='+') {
                placeholder=i;
                break;
            }
            sb.append(c);    
        }
        for(int j=placeholder;j<email.length();j++) {
            char c=email.charAt(j);
            if(c=='@') {
            sb.append(email.substring(j));
            break;
            }
        }
        return sb.toString();

    }
}