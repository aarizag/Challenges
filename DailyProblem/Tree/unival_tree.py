"""
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(head):
    solution.unival_trees = 0

    def inner(node):
        if node is None:
            return None
        l, r = inner(node.left), inner(node.right)
        l = node.val if l is None else l
        r = node.val if r is None else r

        if l == node.val == r:
            solution.unival_trees += 1
        return node.val

    inner(head)
    return solution.unival_trees


def test():
    test_node = Node(1, left=Node(2,
                                  left=Node(2), right=Node(2)),
                        right=Node(3,
                                   left=Node(4), right=Node(5))
                     )
    total = solution(test_node)

    try:
        assert total == 5
        print("Test Passed")
    except AssertionError:
        print(f"Expected 5 subtrees, got {total}.")


test()
