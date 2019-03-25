from typing import TypeVar
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:  # 108 ms
        if l1 is None and l2 is None and carry == 0:
            return None
        else:
            l1 = l1 if l1 is not None else ListNode(0)
            l2 = l2 if l2 is not None else ListNode(0)
            car, val = divmod(l1.val + l2.val + carry, 10)
            node = ListNode(val)
            node.next = self.addTwoNumbers(l1.next, l2.next, car)
            return node

    def withgenerator(self, l1, l2):  # 116 ms
        def generate(node):
            while True:
                if node is None:
                    yield None
                else:
                    yield node.val
                    node = node.next

        node1, node2 = generate(l1), generate(l2)

        def sum_nodes(carry=0):
            v1, v2 = next(node1), next(node2)
            if v1 is None and v2 is None and carry == 0:
                return

            v1, v2 = 0 if v1 is None else v1, 0 if v2 is None else v2
            car, val = divmod(v1+v2 + carry, 10)
            cur = ListNode(val)
            cur.next = sum_nodes(car)
            return cur

        head = sum_nodes()
        return ListNode(0) if head is None else head

    def breakdown(self, l1, l2):  # 116 ms
        def to_num(node):
            i, sum = 0, 0
            while node is not None:
                sum += node.val * (10 ** i)
                i += 1
                node = node.next
            return sum

        def to_nodes(n):
            if n == 0:
                return
            n, val = divmod(n, 10)
            head = ListNode(val)
            head.next = to_nodes(n)
            return head

        head = to_nodes(to_num(l1) + to_num(l2))
        return ListNode(0) if head is None else head



def make_nodes(l):
    if not l:
        return
    head = ListNode(l[0])
    head.next = make_nodes(l[1::])
    return head

l1 = make_nodes([1,2,3])
l2 = make_nodes([4,5,6])

l3 = make_nodes([1,6,0,3,3,6,7,2,0,1])
l4 = make_nodes([6,3,0,8,9,6,6,9,6,1])

sol = Solution()

sol1 = sol.addTwoNumbers(l1,l2)
sol2 = sol.breakdown(l1,l2)
sol3 = sol.withgenerator(l3,l4)

while sol3 is not None:
    print(sol3.val)
    sol3 = sol3.next