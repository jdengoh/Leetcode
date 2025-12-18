class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_dict = {}

        for num in nums:
            if num in seen_dict:
                return True

            seen_dict[num] = 1

        print(seen_dict.values())
        return False
