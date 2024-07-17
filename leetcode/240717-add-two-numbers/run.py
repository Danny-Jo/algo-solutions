from solution import addTwoNumbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

t1_l1 = create_linked_list([2,4,3])
t1_l2 = create_linked_list([5,6,4])

t2_l1 = create_linked_list([0])
t2_l2 = create_linked_list([0])

t3_l1 = create_linked_list([9,9,9,9,9,9,9])
t3_l2 = create_linked_list([9,9,9,9])

test = [[t1_l1, t1_l2], [t2_l1, t2_l2], [t3_l1, t3_l2]]


def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

for i in test:
    print_linked_list(addTwoNumbers(i[0], i[1]))