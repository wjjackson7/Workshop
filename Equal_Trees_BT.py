'''
Given two binary trees, write a function to check if they are the same or not.

Example 1:

         tree 1    tree 2
Input:     1         1
          / \       / \
         2   3     2   3
         
         root1      root2

Output: true



Example 2:

Input:     1         1
          /           \
         2             2

Output: false



Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

Output: false
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isSameTree(p, q):
    
    if p == q == None:
        return True
    elif p is None or q is None:
        return False
        
    if p.value != q .value:
        return False
    
    return isSameTree(p.right,q.right) and isSameTree(p.left,q.left)
    
root1 = Node(33)
root1.left = Node(10)
root1.right = Node(60)
root1.left.left = Node(10)
root1.right.left = Node(40)
root2 = Node(33)
root2.left = Node(10)
root2.right = Node(60)
root2.left.left = Node(15)
root2.right.left = Node(40)
root2.right.right = Node(2)
print(isSameTree(root1, root2))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
