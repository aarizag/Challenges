"""
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all
    of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked

    lock, which attempts to lock the node. If it cannot be locked, then it should return false.
        Otherwise, it should lock it and return true.

    unlock, which unlocks the node. If it cannot be unlocked, then it should return false.
        Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
    You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
    Each method should run in O(h), where h is the height of the tree.
"""


class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
        self.locked = False

    def is_locked(self):
        return self.locked

    def lockable(self):
        def check_parents(node: Node):  # returns False if no ancestor is locked
            return node.is_locked() or check_parents(node.parent) \
                if node else False

        def check_children(node: Node):  # returns False if no child is locked
            return node.is_locked() or check_children(node.left) or check_children(node.right) \
                if node else False

        return not check_parents(self) or not check_children(self)

    def lock(self):
        if self.lockable():
            self.locked = True
            return True
        return False

    def unlock(self):
        if self.lockable():
            self.locked = False
            return True
        return False

    def __str__(self):
        return f"{self.val}{'L' if self.locked else 'U'}"


def iterative_traversal(node):
    stack = [node]
    while stack:
        n = stack.pop()
        if n.right:
            stack.append(n.right)
        if n.left:
            stack.append(n.left)
        print(n)


root = Node(1)
root.left = Node(2, root)
root.right = Node(3, root)
root.left.left = Node(4, root.left)
root.left.right = Node(5, root.left)
root.right.left = Node(6, root.right)
root.right.right = Node(7, root.right)
root.left.left.left = Node(8, root.left.left)
root.left.left.right = Node(9, root.left.left)
root.right.left.right = Node(10, root.left.right)
root.right.right.left = Node(11, root.right.right)

print(root.right.left.lock())
print(root.right.lock())
iterative_traversal(root.right)
print(root.right.left.right.lock())
print(root.right.left.unlock())
