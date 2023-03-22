# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def split(node):
            if not node or not node.next:
                return node
            mi = mid(node)
            left = split(node)
            right = split(mi)
            return merge(left,right)
        def merge(node1,node2):
            dummy = ListNode(0)
            du = dummy
            while node1 and node2:
                if node1.val < node2.val:
                    du.next = node1
                    du = du.next
                    node1 = node1.next
                else:
                    du.next = node2
                    du = du.next
                    node2 = node2.next
            if node1:
                du.next = node1
            else:
                du.next = node2
            return dummy.next
        def mid(node):
            slow = None
            while node and node.next:
                slow = node if not slow else slow.next
                node = node.next.next
            mid = slow.next
            slow.next = None
            return mid
        return split(head)