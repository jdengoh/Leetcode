class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        The idea of this implementation is to initialize a hash table to keep the count of every alphebets (at most 26)

        For s, we +1 for every character iterated
        For t, we -1 for every character instead

        If they are anagram of each other, all element in the table should be 0

        Notes:
        - ord() function returns the number representing the unicode code of a specified character
        """
        # Base condition
        if len(s) != len(t):
            return False

        # Initialize hash table
        count = [0] * 26

        # Iterate length of s (which is also equals to length of t)
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for i in count:
            if i != 0:
                return False
        return True
