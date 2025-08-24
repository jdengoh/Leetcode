class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        We can use a 2 pointer strategy to solve this question.
        - first pointer starts at the start
        - second pointer starts from the end

        Terminating condition will be when first pointer meets the
            second pointer:
        - check using `l<r` or `not l>=r`

        Things to note:
        - we have to check if character is alphanumeric, because
            punctuations should be ignored
        - letter case should not metter, so we can just compare the
            lower case of all letters with .lower()
        """
        # Define pointers
        l = 0
        r = len(s) - 1

        while l < r:
            # Check alphanumeric
            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            if not self.isAlphaNum(s[r]):
                r -= 1
                continue

            # Terminating conidition
            if s[l].lower() != s[r].lower():
                return False

            # Move pointers
            l += 1
            r -= 1

        return True

    def isAlphaNum(self, char):
        """
        checks for:
        - Upper case character
        - lower case character
        - number
        """
        return (
            (ord("A") <= ord(char) <= ord("Z"))
            or (ord("a") <= ord(char) <= ord("z"))
            or (ord("0") <= ord(char) <= ord("9"))
        )
