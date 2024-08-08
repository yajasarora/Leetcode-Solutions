class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wtoc = {}
        word = s.split()
        set1 = set()

        if len(pattern) != len(word):
            return False
        for i in range(len(word)):
            if word[i] in wtoc:
                if wtoc[word[i]] != pattern[i]:
                    return False
            else:
                if pattern[i] in set1:
                    return False
                wtoc[word[i]] = pattern[i]
                set1.add(pattern[i])
        return True
