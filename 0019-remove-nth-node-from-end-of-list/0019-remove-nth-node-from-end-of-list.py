# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        for i in range(0, n):
            first = first.next

        if not first:
            temp = head
            if not head.next:
                head = None
                return head
            else:
                temp = head
                head = head.next
                return head
       
        second = head
        #pointer second to get to the node before the one we want to delete
        while first and first.next:
            first = first.next
            second = second.next
        #increment first and second first should be last node and
        #second should be the node before the one we want to delete
    
        second.next = second.next.next
        #have second.next be the node after one to delete to delete that node

        return head