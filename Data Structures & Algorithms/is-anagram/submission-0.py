class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = Counter(s)
        t_counts = Counter(t)

        return True if s_counts == t_counts else False