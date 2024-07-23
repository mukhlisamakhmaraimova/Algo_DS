class ListNode:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head) -> None:  # 1chi element head db ataladi, linked listni boshlanishi, kngi qiymat next, next bop keturadi
        self.head = head
        self.counter = 1
        self.summa = head.data

    def print_nodes(self):   # qiymatlarni chop etadigan funksiya
        x = self.head
        while x:
            print(x.data, end='\t')
            x = x.next
        print()

    def add_item_to_start(self, new_head):  # boshiga yangi elememt qoshish
        # x = self.head
        self.counter += 1
        self.summa += new_head
        self.head = ListNode(new_head, self.head)
        # self.head.next = x

    def add_item(self, new_node, node): # Pythdan kn yangi element qoshish
        self.counter += 1
        self.summa += new_node
        x = self.head
        while x.data != node:
            x = x.next
        x.next = ListNode(new_node, x.next)

    def add_item_to_end(self, new_node):  # oxiriga yangi element qoshish
        self.counter += 1
        self.summa += new_node
        x = self.head
        while x.next:
            x = x.next
        x.next = ListNode(new_node)

    def sum(self):
        return self.summa
        # s = 0
        # x = self.head
        # while x:
        #     s += x.data
        #     x = x.next
        # return s

    # def sum_len(self):
    #     s = 0
    #     l = 0
    #     x = self.head
    #     while x:
    #         s += x.data
    #         l += 1
    #         x = x.next
    #     return s, l

    def __len__(self):  # len -> override boldi
        return self.counter
        # s = 0
        # x = self.head
        # while x:
        #     s += 1
        #     x = x.next
        # return s

# head = ListNode('Python')
head = ListNode(10)

ll = LinkedList(head)

# print(ll.head.data)
# print(ll.head.next)

ll.print_nodes()
ll.add_item_to_end(int(input("Insert new node: ")))
# ll.add_item_to_end(input("Insert new node: "))
ll.print_nodes()
ll.add_item_to_start(int(input("Insert new head: ")))
ll.print_nodes()
ll.add_item(int(input("Insert new node: ")), int(input('After which element: ')))
ll.print_nodes()
print(ll.sum())
# print(ll.sum_len())
print(len(ll))