'''
Given a binary tree, determine if it is height-balanced.
Example 1:


    3
   / \
  9  20
    /  \
   15   7

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isBalanced(root):
    if root is None:
        return
    
    isBalanced(root.right)
    isBalanced(root.left)
    if get_height(root.left)+1 < get_height(root.right) or get_height(root.left)-1 > get_height(root.right):
        return False
    return True
    
    
        
def get_height(root):
    if root is None:
        return 0
    left = get_height(root.left)
    right = get_height(root.right)
    return max(left,right)+1
    
        
root = Node(33)
root.left = Node(10)
root.right = Node(60)
root.left.left = Node(10)
root.right.left = Node(40)
print(isBalanced(root))



