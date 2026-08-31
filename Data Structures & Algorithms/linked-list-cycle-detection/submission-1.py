# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
        # list=[]
        # while head:
        #     if head.val in list:
        #         return True
        #     else:
        #         list.append(head.val)
        #         if head.next==None:
        #             return False
        #         head=head.next    