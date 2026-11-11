class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Sliding window method with a twist

        The sliding window in this case is tracked by the index saved in a hashmap/dict.
        * Movement of `l` is now instant and optimal

        By initializing r=0 and r<len(s), this accounts for edge cases:
        * len(s) == 0
        * len(s) == 1

        Time complexity: O(n)
        Space complexity: O(m) -> unique char saved in `seen`

        """

        occurrence_map = {}
        longest_substring = 0

        l = 0

        for r in range(len(s)):

            if s[r] in occurrence_map:
                # intersting scenario
                # - we never remove stale characters when using this map method
                # - when we encounter a "duplicate", it might be a stale character behind our current `l`
                # - check, if `l` is ahead of the duplicate occurance recorded, sage to ignore, keep `l` where it is, hence the use of max
                l = max(l, occurrence_map[s[r]] + 1)

            occurrence_map[s[r]] = r
            longest_substring = max(longest_substring, r - l + 1)

        return longest_substring
