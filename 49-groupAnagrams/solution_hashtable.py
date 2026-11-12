class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Hashtable method

        Time complexity: O(n * k)
        Space complexity: O(n * k)

        Where n is the number of strings and k is the longest string

        """
        result = defaultdict(list)

        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord("a")] += 1

            # bug 1: cannot use a list as a dictionary key, so change to tuple
            # bug 2: tried using .join() to create a string, but char_count has a list of integer
            #   - "1,11,0,..." and "11,1,0,..." will produce the same "string" despite having different char count,
            #      so it is important to preserve the separator
            #   - best is to use a tuple to preserve it
            result[tuple(char_count)].append(s)

        return list(result.values())
