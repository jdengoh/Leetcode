class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Hashmap method, only one pass

        Time complexity: O(n)
        Space complexity: O(n)

        """

        enum_list = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in enum_list:
                return [min(i, enum_list[diff]), max(i, enum_list[diff])]

            enum_list[num] = i

        # Older loop used, but not ideal

        # for i in range(len(nums)):
        #     diff = target - nums[i]

        #     if diff not in enum_list:
        #         enum_list[nums[i]] = i
        #     else:
        #         return [
        #             min(i, enum_list[diff]),
        #             max(i, enum_list[diff])
        #         ]
