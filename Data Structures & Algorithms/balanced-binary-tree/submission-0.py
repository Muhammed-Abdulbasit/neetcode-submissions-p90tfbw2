# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
U: 1 node or no nodes should return true

M: recursion to traverse tree
- post order traversal
    - need to have depth of left subtree
    - and of right subtree
    - at current node calculate depth of both sides if still balanced
- bottom up; bubbling from bottom passing depth + 1

P:
- If root is null, return true
- recursive helper function
- base condition: if node is empty return 0
- recurse on left node, then right (returns depth or a negative value to indicate
depth or not balanced)
- if left or right subtree returned a -1. return -1
- abs(left - right) > return -1
- return 1 + max(height)

"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            l = dfs(node.left)
            r = dfs(node.right)

            if l < 0 or r < 0:
                return -1
            elif abs(l-r) > 1:
                return -1
            else:
                return 1+max(l, r)
        return dfs(root) != -1
        