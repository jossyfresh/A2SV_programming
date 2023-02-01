# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1 = []
        list2 = []
        temp1 = head
        temp2 = head
        while temp1!=None:
            if temp1.val < x:
                list1.append(ListNode(temp1.val,None))
            else:
                list2.append(ListNode(temp1.val,None))
            temp1 = temp1.next
        if len(list1) > 0:
            node =  list1[0]
            dhead = ListNode(0,None)
            dhead.next = node
            for i in range(1,len(list1)):
                node.next = list1[i]
                node = node.next
            for j in range(len(list2)):
                node.next = list2[j]
                node = node.next
            return dhead.next
        elif len(list2) > 0:
            node =  list2[0]
            dhead = ListNode(0,None)
            dhead.next = node
            for j in range(1,len(list2)):
                node.next = list2[j]
                node = node.next
            return dhead.next
            
            