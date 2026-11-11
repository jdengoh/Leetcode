class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Time Complexity: O(nlog(n))
        # Space Complexity: O(n)

        enum_list = []

        # What if we were to append as [i, num]

        # for i, num in enumerate(nums):
        #     enum_list.append([i, num])

        # enum_list.sort(key=lambda pair: pair[1])
        # print(enum_list)

        # What if we were to append as [num, i]

        for i, num in enumerate(nums):
            enum_list.append([num, i])

        enum_list.sort()

        i, j = 0, len(enum_list) - 1

        while i < j:
            sum = enum_list[i][0] + enum_list[j][0]

            if sum == target:
                return [
                    min(enum_list[i][1], enum_list[j][1]),
                    max(enum_list[i][1], enum_list[j][1]),
                ]
            elif sum < target:
                i += 1
            else:
                j -= 1

        return None
