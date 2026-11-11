class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Time Complexity: O(n)
        # Space Complexity: O(n)

        indices_dict = {}

        for i, num in enumerate(nums):
            indices_dict[num] = i

        for i in range(len(nums)):
            diff = target - nums[i]

            # 2nd condition is crucial. when we have same value appearing,
            #   we will overwrite the index when adding to indices_dict.
            #   this 2nd conditions ensure that it is correct.
            if diff in indices_dict and indices_dict[diff] != i:
                return [min(i, indices_dict[diff]), max(i, indices_dict[diff])]
