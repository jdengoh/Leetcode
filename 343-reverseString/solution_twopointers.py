class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        We can also use 2 pointer approach:
        - i: starting pointer (i as index)
        - j: ending pointer (j as index)
        """

        # left pointer
        left = 0
        # right pointer
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
