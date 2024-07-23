class ListNode:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head) -> None:
        self.head = head

    def print_items(self):
        x = self.head

        while x:
            print(x.data)
            x = x.next

head = ListNode('Dushanba')

week = LinkedList(head=head)
week.head.next = ListNode('Seshanba')
week.head.next.next = ListNode('Chorshanba')

# print(week.head.data)
# print(week.head.next.data)
# print(week.head.next.next.data)

h = input('Insert days: ').split()
week.print_items()

print('\n\n')
x = head
for day in h:
    x.next = ListNode(day)
    x = x.next

week.print_items()