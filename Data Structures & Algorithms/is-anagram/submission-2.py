class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}
        i, j = 0, 0

        while i < len(s):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1
            i += 1

        while j < len(t):
            if t[j] in count:
                count[t[j]] -= 1
                if count[t[j]] < 0:
                    return False
            else:
                return False
            j += 1
        
        return True