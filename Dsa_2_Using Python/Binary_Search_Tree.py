class Node:
    def __init__(self,key):
        self.left=None
        self.key=key
        self.right=None
def insert_(root,key):
    if root is None:
        return Node(key)
    elif key<root.key:
        root.left=insert_(root.left,key)
    else:
        root.right=insert_(root.right,key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.key)+"->",end="")
        inorder(root.right)
def get_min_value(root):
    while root.left:
        root=root.left
    return root
def delete(root,value):
    if root is None:
        return root
    elif value<root.key:
        root=delete(root.left,value)
    elif value>root.key:
        root=delete(root.right,value)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp==root.left
            root=None
            return temp
        
        temp=get_min_value(root.right)
        root.val=temp.val
        root.right=delete(root.right,temp.val)
    return root  


            

root=None
root=insert_(root,8)
root=insert_(root,3)
root=insert_(root,1)
root=insert_(root,6)
root=insert_(root,7)
root=insert_(root,10)
root=insert_(root,14)
root=insert_(root,4)
delete(root,14)
inorder(root)
