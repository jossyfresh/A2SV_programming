# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp1 = head
        new = []
        while temp1!=None:
            new.append(ListNode(temp1.val,None))
            temp1 = temp1.next
        check = new[-1]
        dhead = ListNode(0,None)
        dhead.next = check
        for i in range(len(new)-2,-1,-1):
            check.next = new[i]
            check = check.next
        check = dhead.next
        while head!=None:
            if head.val != check.val:
                return False
            check = check.next
            head = head.next
        return True
        