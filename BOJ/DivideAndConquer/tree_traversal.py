class node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):
    print(node.data, end=' ')
    if node.left != None:
        pre_order(node.left)
    if node.right != None:
        pre_order(node.right)
def in_order(node):
    if node.left != None:
        in_order(node.left)
    print(node.data, end=' ')
    if node.right != None:
        in_order(node.right)
def post_order(node):
    if node.left != None:
        post_order(node.left)
    if node.right != None:
        post_order(node.right)
    print(node.data, end=' ')
    
