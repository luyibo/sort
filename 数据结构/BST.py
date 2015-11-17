# -*- coding:utf-8 -*-
__author__ = 'apple'
class Tree:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def insert(root,val):
    if root is None:
        root=Tree(val)
    else:
        if val<root.val:
            root.left=insert(root.left,val)
        elif val>root.val:
            root.right=insert(root.right,val)
    return root

def query(root,val):
    if root is None:
        return
    if root.val==val:
        return 1
    else:
        if root.val<val:
            return query(root.right,val)
        else: return query(root.left,val)

def findmin(root):
    if root.left:
        findmin(root.left)
    else:
        return root

def delnum(root,val):
    if root is None:
        return
    if val<root.val:
         return delnum(root.left,val)
    elif val>root.val:
         return delnum(root.right,val)
    else:
        if (root.left and root.right):
            tmp=findmin(root.right)
            root.val=tmp.val
            root.right=delnum(root.righr,val)
        else:
            if root.left is None:
                root=root.right
            elif root.right is None:
                root=root.right
    return root
root=Tree(3)
root=insert(root,2)
root=insert(root,1)
root=insert(root,4)
print query(root,2)
root=delnum(root,1)
print query(root,1)

