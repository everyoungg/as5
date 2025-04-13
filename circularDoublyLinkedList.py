
class Node:
    def __init__(self, name, birthday, group):
        self.name = name
        self.birthday = birthday
        self.group = group
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, birthday, group):
        new_node = Node(name, birthday, group)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def print_group(self, group_number):
        if not self.head:
            return
        current = self.head
        while True:
            if current.group == group_number:
                print(f"이름: {current.name}, 생년월일: {current.birthday}")
            current = current.next
            if current == self.head:
                break
