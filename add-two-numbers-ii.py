# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0,None)
        res = ListNode(0,None)
        res.next = ans
        def reverse(node):
            current = node
            previous = None
            following = current.next
            while current:
                current.next = previous
                previous = current
                current = following
                if following:
                    following = following.next
            return previous
        l1 = reverse(l1)
        l2 = reverse(l2)
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val > 9:
                ans.next = ListNode(val%10)
                carry = 1
            else:
                ans.next = ListNode(val)
                carry = 0
            ans = ans.next
            l2 = l2.next
            l1 = l1.next
        while l1:
            val = l1.val + carry
            if val > 9:
                ans.next = ListNode(val % 10)
                carry = 1
            else:
                ans.next = ListNode(val)
                carry = 0
            ans = ans.next
            l1 = l1.next
        while l2:
            val = l2.val + carry
            if val > 9:
                ans.next = ListNode(val % 10)
                carry = 1
            else:
                ans.next = ListNode(val)
                carry = 0
            l2 = l2.next
            ans = ans.next
        if carry:
            ans.next = ListNode(carry)
        return reverse(res.next.next)