from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# * 아래 코드는 l1, l2가 list일 때로 착각하고 작업한 내용이다.  
# def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#     num1 = ''.join(list(map(str, l1[::-1])))
#     num2 = ''.join(list(map(str,l2[::-1])))
#     total = int(num1) + int(num2)
#     result = list(map(int, str(total)[::-1]))
#     return result

# * 위 코드와 문제 해결하는 과정은 사실상 동일하다.
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def list_to_reversed_str(node: ListNode) -> str:
            num_str = ''
            while node:
                num_str = str(node.val) + num_str
                node = node.next
            return num_str

    num1 = list_to_reversed_str(l1)
    num2 = list_to_reversed_str(l2)

    total = int(num1) + int(num2)

    dummy_head = ListNode(0)
    current = dummy_head
    for digit in str(total)[::-1]:
        current.next = ListNode(int(digit))
        current = current.next
        
    return dummy_head.next