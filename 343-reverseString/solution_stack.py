class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        We can use a "stack" implementation with python lists
        
        However, this still requires an additional list to be created
        """

        stack_list = []

        for i in s:
            stack_list.append(i)

        j=0
        while stack_list:
            s[j] = stack_list.pop()
            j+=1
