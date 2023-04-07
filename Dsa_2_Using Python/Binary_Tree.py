class Node:
    def __init__(self,item):
        self.left=None
        self.data=item
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data)+"->",end="")
        inorder(root.right)
def preorder(root):
    if root:
        print(str(root.data)+"->",end="")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data)+"->",end="")

n=Node(1)
n.left=Node(2)
n.right=Node(3)
n.left.left=Node(4)
n.left.right=Node(5)
print('Inorder')
print(inorder(n))
print('preorder')
print(preorder(n))
