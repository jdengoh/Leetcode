class Solution:
    def isValid(self, s: str) -> bool:
        """Stack method

        Time complexity: O(n)
        Space complexity: O(n)

        """

        stack = []
        pairing_dict = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        # Probably not needed but good to consider
        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in pairing_dict:
                # bug: remember to check and make sure stack even exist...
                if stack and pairing_dict[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        # bug: must check and ensure that stack is empty
        # * edge case where we only have opening paranthesis but no closing at all
        # * the opening will remain inside without any pop happening, and loop will exit

        # return True if not stack else False
        return not stack
