# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        curr = root
        stack = []
        res = set()

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.add(curr.val)
            curr = curr.right
        

        if len(res) > 1:
            return sorted(list(res))[1]
        
        return -1