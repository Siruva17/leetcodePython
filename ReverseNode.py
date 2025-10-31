# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Step 1: Check if we have k nodes available
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head  # Not enough nodes left, return as-is

        # Step 2: Reverse k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Recursively reverse the remaining list
        head.next = self.reverseKGroup(curr, k)

        # Step 4: Return the new head (which is prev after reversal)
        return prev
