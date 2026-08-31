class Solution:
    def get_length(self, head):              # FIX 1: add self
        count = 0
        current = head

        while current is not None:
            count += 1
            current = current.next

        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = ListNode(), head

        l = self.get_length(head)
        c = l - n

        # FIX 2: handle removing the first node
        if c == 0:
            return head.next

        # FIX 3: move to the node that needs to be removed
        for i in range(c):
            prev = curr
            curr = curr.next

        # Remove curr
        prev.next = curr.next

        return head