class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node("HEAD")
        self.tail = self.head
        self.number_of_nodes = 0

    def append(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.increase_number_of_nodes()

    def delete(self, data):
        node = self.head
        while node.next is not None:
            if node.next.data is data:
                node.next = node.next.next
                self.decrease_number_of_nodes()
                break
            node = node.next
        if not self.tail:
            self.tail = self.head

    def is_contain(self, data):
        node = self.head
        while node.next is not None:
            if node.next.data is data:
                return True
            node = node.next
        return False

    def get(self, index):
        node = self.head.next
        count = 0
        for i in range(self.number_of_nodes):
            if count == index:
                return node.data
            node = node.next
            count += 1

    def get_all(self):
        el = []
        node = self.head
        while node.next is not None:
            el.append(node.next.data)
            node = node.next
        return el

    def size(self):
        return self.number_of_nodes

    def increase_number_of_nodes(self):
        self.number_of_nodes += 1

    def decrease_number_of_nodes(self):
        self.number_of_nodes -= 1


if __name__ == '__main__':
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    print(list.size())
    list.delete(3)
    print(list.get_all())
    list.delete(5)
    print(list.get_all())