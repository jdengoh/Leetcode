class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Sliding window method

        This method is shrinks window in a loop

        By initializing r=0 and r<len(s), this accounts for edge cases:
        * len(s) == 0
        * len(s) == 1

        Time complexity: O(n)
        Space complexity: O(m) -> unique char saved in `seen`

        """

        seen = set()
        longest_substring = 0

        l = 0

        for r in range(len(s)):

            while s[r] in seen:
                # bug here previously! remove s[l] first before moving l forward
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            # (r - 1 + 1) needs to add 1 to account for shifting l forward already
            longest_substring = max(longest_substring, r - l + 1)

        return longest_substring
