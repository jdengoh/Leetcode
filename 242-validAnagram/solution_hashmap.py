class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Base condition
        if len(s) != len(t):
            return False

        # Initialize hashmaps
        s_map = {}
        t_map = {}

        # Iterate length of s (which is also equals to length of t)
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1

        # Compare hashmaps and return
        return s_map == t_map
