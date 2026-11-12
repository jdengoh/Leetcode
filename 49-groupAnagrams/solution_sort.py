class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Sorting method

        Time complexity: O(n klog(k))
        Space complexity: O(n * k)

        Where n is the number of strings and k is the longest string

        """
        result = defaultdict(list)

        for s in strs:
            # sort each string using sorted()
            sorted_str = "".join(sorted(s))
            # using the sorted string as the key, append the original string as value
            result[sorted_str].append(s)

        # res.values() returns a view object on all the values, and list converts it into a list
        return list(result.values())
