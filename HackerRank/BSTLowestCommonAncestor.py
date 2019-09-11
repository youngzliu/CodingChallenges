

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def contains(root, val):
    if (root == val):
        return True
    elif (root.left == None and root.right == None):
        return False
    elif (root.left != None and val < root.info):
        return contains(root.left, val)
    elif (root.right != None and val > root.info):
        return contains(root.right, val)
    else:
        return False

def lca(root, v1, v2):
    if(v1 < root.info and v2 < root.info and root.left != None):
        return lca(root.left, v1, v2)
    if(v1 > root.info and v2 > root.info and root.right != None):
        return lca(root.right, v1, v2)
    return root


