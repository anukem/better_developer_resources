# https://leetcode.com/problems/add-two-numbers/
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode()
    current = head
    carry = 0
    while l1 or l2:
        left = l1.val if l1 else 0
        right = l2.val if l2 else 0
        if left + right + carry < 10:
            current.val = left + right + carry
            carry = 0
        else:
            current.val = (left + right + carry) % 10
            carry = 1
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        if l1 or l2:
            current.next = ListNode()
            current = current.next
    if carry:
        current.next = ListNode()
        current = current.next
        current.val = 1
    return head


