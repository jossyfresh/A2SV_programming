# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        r = 1
        temp1 = head
        temp2 = head
        while i < left:
            temp1 = temp1.next
            i+=1
        while r < right:
            temp2 = temp2.next
            r+=1
        if left == 1:
            temp = ListNode(temp2.val,None)
            temp3 = temp2.next
            lin = []
            dhead = ListNode(0,None)
            dhead.next = temp
            i = 0
            n = right-2
            while n >= i:
                j = i
                temp1 = head
                while j < n:
                    temp1 = temp1.next
                    j+=1
                n-=1
                lin.append(ListNode(temp1.val,None))
            for x in lin:
                temp.next = x
                temp = temp.next
            temp.next = temp3
            return dhead.next
        elif left == right:
            return head
        else:   
            temp3 = temp2.next
            new =[]
            temp1 = head
            duhead = ListNode(0,None)
            duhead.next = temp1
            i = 1
            temp4 = temp1
            while i < left-1:
                temp4 = temp4.next
                i+=1
            while right >= left:
                j = left-1
                temp = temp4
                while j < right:
                    temp = temp.next
                    j+=1
                right-=1
                new.append(ListNode(temp.val,None))
            for x in new:
                temp4.next = x
                temp4 = temp4.next
            temp4.next = temp3
            return duhead.next

                
                    
            
            
        
            
            