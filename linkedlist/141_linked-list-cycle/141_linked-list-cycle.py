
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head): 
        slow , fast = head, head
        while fast and fast.next:
            slow  = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    head = [5,4,3,2,1]
    print(solution.hasCycle(head))