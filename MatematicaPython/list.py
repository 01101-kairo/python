class Node:
    def __init__(self, vol, next=None):
        self.vol = vol
        self.next = next


head = Node(0)
i = 1
atual = head
while i < 1000:
    atual.next = Node(i)
    atual = atual.next
    i += 1


atual2 = head
while atual2:
    print(atual2.vol)
    atual2 = atual2.next
