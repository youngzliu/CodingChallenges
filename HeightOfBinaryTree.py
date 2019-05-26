

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if(root.left == None and root.right == None):
        return 0
    elif(root.left == None):
        return 1 + height(root.right)
    elif(root.right == None):
        return 1 + height(root.left)
    else:
        return 1 + max(height(root.left), height(root.right))

