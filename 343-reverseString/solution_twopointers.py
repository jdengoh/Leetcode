class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        We can also use 2 pointer approach:
        - i: starting pointer (i as index)
        - j: ending pointer (j as index)
        """

        # left pointer
        l = 0
        # right pointer
        r = len(s) - 1

        while l<r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1