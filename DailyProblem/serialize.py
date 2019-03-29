"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
    which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def iterative_traversal(node):
    stack = [node]
    while stack:
        n = stack.pop()
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
        print(n.val)


def serialize(node: Node) -> str:
    if not node:
        return "None"
    return f"{node.val},{serialize(node.left)},{serialize(node.right)}"


def deserialize(n_string: str) -> Node:
    spl = n_string.split(",")

    def inner():
        if not spl:
            return None
        val, parent = spl.pop(0), None
        if val != "None":
            parent = Node(val, inner(), inner())
        return parent

    return inner()


node = Node('root', Node('left', Node('left.left'), Node("left.right")),
            Node('right', Node("right.left"), Node("right.right", None, Node("right.right.right"))))
print("Node")
iterative_traversal(node)
print("\nDeserialized")
iterative_traversal(deserialize(serialize(node)))
print(deserialize(serialize(node)).left.left.val == 'left.left')
