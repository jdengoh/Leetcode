class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Sliding window method

        This method is shrinks window one at a time

        By initializing r=0 and r<len(s), this accounts for edge cases:
        * len(s) == 0
        * len(s) == 1

        Time complexity: O(n)
        Space complexity: O(m) -> unique char saved in `seen`

        """

        seen = set()
        longest_substring = 0

        # Initialize both at start (so window is only 1 element wide initially)
        l, r = 0, 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                longest_substring = max(longest_substring, r - l)

            else:
                seen.remove(s[l])
                l += 1

        return longest_substring
