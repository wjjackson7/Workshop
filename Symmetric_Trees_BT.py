'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

       1
      / \
     /   \
    /     \
   /       \
  2         2
 / \       / \
3   4     4   3

n1.left n2.right
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
 / \   \
3   3   3
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isSymmetric(root):
    if root is None:
        return True
    
    return areEqual(root.left,root.right)


def areEqual(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    
    left = areEqual(node1.right, node2.left)
    right = areEqual(node1.left,node2.right)
    return left and right and node1.value == node2.value
     
root1 = Node(33)
root1.left = Node(60)
root1.right = Node(60)
root1.left.left = Node(10)
root1.right.left = Node(10)
print(isSymmetric(root1))
     
     
     
     
