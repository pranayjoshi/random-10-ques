
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def prev(root):
    if root:
        prev(root.right)
        print(root.val)
        prev(root.left)



# Driver code
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
root.right.left  = Node(6)
root.right.right  = Node(7)

print("\nImplemented Backward Iterator in BST")
prev(root)
