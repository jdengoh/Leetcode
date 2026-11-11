class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Reverse string method

        Time complexity: O(n)
        Space complexity: O(n)

        """

        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]
