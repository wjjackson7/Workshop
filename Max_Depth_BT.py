# 1. Q1: Maximum Depth of Binary Tree


# Given a binary tree, find its maximum depth. 
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#             3         
#           /   \
#          9      1    
#               /   \
#              15    7







class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        left = self.maxDepth(root.left)
        right= self.maxDepth(root.right)
        return max(left, right) + 1
        
print(maxDepth())
        
