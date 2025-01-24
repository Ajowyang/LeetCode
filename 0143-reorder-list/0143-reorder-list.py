# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow and fast pointers to get the midpoint
     
        second = slow.next
        #node after midpoint is start of 2nd list
        slow.next = None
        #sever connection of first list to split into 2 lists
       
        prev = None
        #create new pointer that starts at none to reverse list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        #reverse order of second list

        second = prev
        first = head
        #pointers start at beginning of each list

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        #merge the 2 lists 1[0], 2[0], 1[1], 2[1], 1[2], 2[2], etc...        
        """
        Do not return anything, modify head in-place instead.
        """
        