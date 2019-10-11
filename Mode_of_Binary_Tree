
'''
      6
  3       20
        12 
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

max_count = 0
max_val = -1
#bad space solution
# dic = {}

# def find_mode(tree):
#     find_mode_recursive(root)
#     print(max(dic.keys(), key=(lambda k: dic[k])))
    
# def find_mode_recursive(tree):
#     if tree.right is None and tree.left is None:
#         return 0
#     else :
#         if tree.value not in dic:
#             dic[tree.value] = 1
#         else:
#             dic[tree.value] = dic.get(tree.value)+1
    
#     if tree.left is not None:
#         find_mode_recursive(tree.left)
#     if tree.right is not None:
#         find_mode_recursive(tree.right)

def find_mode(tree):
    global max_count
    global max_val
    
    max_val = 0;
    max_count = 0;
    find_mode_recursive(tree, 1, 1);
    print("winner is "+str(max_val)+" with count of "+str(max_count));
    
def find_mode_recursive(tree, cur_val, cur_count):
    global max_count
    global max_val
    cur_c = cur_count
    cur_v = cur_val
    
    if tree == None:
        return
    
    
    if cur_v == tree.value:
        cur_c+=1
        find_mode_recursive(tree.left,tree.value, cur_c)
        if cur_c > max_count:
            max_count = cur_c
            max_val = cur_v
    else:
        find_mode_recursive(tree.left,tree.value, cur_c)
        cur_v = tree.value
        cur_c = 1
    
    
    print(str(tree.value)+" - current is "+str(cur_v)+" with count of "+str(cur_c))
    find_mode_recursive(tree.right,cur_v, cur_c)
    
    
    
root = Node(33)
root.left = Node(10)
root.right = Node(60)
root.left.left = Node(10)
root.right.left = Node(40)
root.right.left.left = Node(40)
root.right.left.left.left = Node(40)
root.right.left.left.left.left = Node(40)
print(find_mode(root))
    
    
