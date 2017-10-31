""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return isBST(root, -1, 10001)

def isBST(root, lo, hi):
    if root == None:
        return True
    if root.data <= lo or root.data >= hi:
        return False
    return isBST(root.left, lo, root.data) and isBST(root.right, root.data, hi)