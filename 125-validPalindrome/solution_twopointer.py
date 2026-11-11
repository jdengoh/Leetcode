class Solution:

    def isPalindrome(self, s: str) -> bool:
        """Two pointer method

        Time complexity: O(n)
        Space complexity: O(1)

        Important pointers:
        * account for speical characters (punctuations, white space, etc...)
        * upper and lower case should be ignored

        Trick to this question is to use `ord()` function to get the ASCII code
        * 48-57   -> '0'-'9'
        * 65-90   -> 'A'-'Z'
        * 97-122  -> 'a'-'z'

        """

        l = 0
        r = len(s) - 1

        while l < r:

            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            if not self.isAlphaNum(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isAlphaNum(self, c: str) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )
