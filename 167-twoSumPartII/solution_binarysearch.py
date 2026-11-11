class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """Binary search method

        Time complexity: O(nlog(n))
        - Binary search is O(log(n)) search time
        - Since we will do binary search for up to n times, hence the stated time complexity

        Space complexity: O(1)

        """

        for i in range(len(numbers)):

            # left and right bound for the binary search afterwards
            l, r = i + 1, len(numbers) - 1

            diff = target - numbers[i]

            # inner loop that handles binary serach for the targetted diff value
            # binary search time complexity is O(log(n))
            while l <= r:

                # get mid index
                mid = l + (r - l) // 2

                if numbers[mid] == diff:
                    return [i + 1, mid + 1]
                elif numbers[mid] < diff:
                    l = mid + 1
                else:
                    r = mid - 1
