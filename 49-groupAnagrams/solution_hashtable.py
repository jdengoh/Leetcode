class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use a dictionary to group anagrams by character frequency.

        For each string, create a frequency array of 26 characters (a-z).
        Use this frequency tuple as the key to group anagrams together.

        Complexity:
        - Time: O(m * n) where m is number of strings, n is string length
        """
        anagram_dict = defaultdict(list)

        for s in strs:
            # initialize a list of unique occurrence count
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1

            # append to dict or list, using the unique occurrence tuple
            #  as the dict key
            anagram_dict[tuple(count)].append(s)

        return list(anagram_dict.values())
