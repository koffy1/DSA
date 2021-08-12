# https://leetcode.com/problems/sort-list/submissions/

# Solution using bubble sort

''' This solution timed out on leet code for a larger input
    because the time complexity for this algorithm is O(n^2)'''

class Solution:
    def sortList(self, head):
        if head is None:
            return head
        while True:
            current = head
            swap = 0
            while current.next is not None:
                if current.val > current.next.val:
                    temp = current.val
                    current.val = current.next.val
                    current.next.val = temp
                    swap = 1
                current = current.next
            if swap == 0:
                break
        return head