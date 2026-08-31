# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         last,prev= ListNode(),ListNode()
#         start=head
#         while start and start.next and start.next.next:
#             prev=start
#             head=start.next
#             while head.next:
#                 prev=head
#                 head=head.next
#             prev.next=None
#             head.next=start.next
#             start.next=head

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start = head
        while start and start.next and start.next.next:
            prev = start
            curr = start.next
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            curr.next = start.next
            start.next = curr
            start = curr.next