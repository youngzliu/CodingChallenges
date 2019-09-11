""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return checkParams(root, -1, 99999)
    
def checkParams(root, biggerThan, lessThan):
    if(root.left == None and root.right == None):
        return (root.data > biggerThan) and (root.data < lessThan)
    elif(root.left == None):
        return (root.data > biggerThan) and (root.data < lessThan) and checkParams(root.right, max(biggerThan, root.data), lessThan)
    elif(root.right == None):
        return (root.data > biggerThan) and (root.data < lessThan) and checkParams(root.left, biggerThan, min(lessThan, root.data))
    else:
        return (root.data > biggerThan) and (root.data < lessThan) and checkParams(root.right, max(biggerThan, root.data), lessThan) and checkParams(root.left, biggerThan, min(lessThan, root.data))
        
    