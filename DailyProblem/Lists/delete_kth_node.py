"""
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list.
    k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class LinkedNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


def remove_k(node: LinkedNode, k: int) -> LinkedNode:
    if k == 0:
        return node.nxt
    node.nxt = remove_k(node.nxt, k-1)
    return node


def test():
    test_node = LinkedNode(1, LinkedNode(2, LinkedNode(3, LinkedNode(4, LinkedNode(5)))))
    test_node = remove_k(test_node, 2)
    try:
        assert test_node.nxt.nxt.val == 4
        print("test successful")
    except AssertionError:
        print("test failed")


test()
