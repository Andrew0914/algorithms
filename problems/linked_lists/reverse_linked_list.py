from utils.list_node import ListNode


class Solution:
    def reverseList(self, head: ListNode):
        current_head = head
        dummy = None
        while current_head is not None:
            temp = current_head.next
            current_head.next = dummy
            dummy = temp
            current_head = temp
        return dummy

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

s = Solution()
s.reverseList(head)
#print(reversed_head)
