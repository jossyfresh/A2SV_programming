# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0,None)
        dhead = ListNode(0,None)
        dhead.next = ans
        while list1!=None and list2!=None:
            if list1.val < list2.val:
                ans.next = ListNode(list1.val,None)
                ans = ans.next
                list1 = list1.next
            else:
                ans.next = ListNode(list2.val,None)
                ans = ans.next
                list2 = list2.next
        while list1!=None:
            ans.next = ListNode(list1.val,None)
            ans = ans.next
            list1 = list1.next
        while list2!=None:
            ans.next = ListNode(list2.val,None)
            ans = ans.next
            list2 = list2.next
        return dhead.next.next
            
            
                