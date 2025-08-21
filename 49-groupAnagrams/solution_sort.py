class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        We will use a dictionary of lists to "collect" anagrams under the same key
        - To check if they are the anagrams, we can first sort and compare

        Implementation:
        - Use defaultdict(list) to initialize a dictionary of lists
        - If the key doesn't exists, empty list will be created
        - We will simply append to either an existing or empty lists

        Complexity:
        - Time: O(n * m log m), where n is the number of strings and m is the maximum length of a string
        - Space: O(n * m), where n is the number of strings and m is the maximum length of a string
        """
        anagram_dict = defaultdict(list)

        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            anagram_dict[sorted_str].append(strs[i])

        print(anagram_dict)

        return list(anagram_dict.values())
