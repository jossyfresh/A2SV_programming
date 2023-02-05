# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        ans = ListNode(0,None)
        dhead = ListNode(0,None)
        dhead.next = ans
        value = 0
        prev = False
        while temp1!=None and temp2!=None:
            if prev:
                value = temp1.val+temp2.val+1
            else:
                value = temp1.val+temp2.val
            if value > 9:
                prev = True
                ans.next = ListNode(value%10,None)
                ans = ans.next
            else:
                prev = False
                ans.next = ListNode(value,None)
                ans = ans.next
            temp1=temp1.next
            temp2 = temp2.next
        while temp1!=None:
            if prev:
                value = temp1.val+1
            else:
                value = temp1.val
            if value > 9:
                ans.next = ListNode(value%10,None)
                ans = ans.next
                prev = True
            else:
                ans.next = ListNode(value,None)
                ans = ans.next
                prev = False
            temp1 = temp1.next
        while temp2!=None:
            if prev:
                value = temp2.val+1
            else:
                value = temp2.val
            if value > 9:
                ans.next = ListNode(value%10,None)
                ans = ans.next
                prev = True
            else:
                ans.next = ListNode(value,None)
                ans = ans.next
                prev = False
            temp2 = temp2.next
        if prev:
            ans.next = ListNode(1,None)
            ans = ans.next
        return dhead.next.next
                