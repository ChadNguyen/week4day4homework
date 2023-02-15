class LinkedNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def append_node(self, value):
        node = LinkedNode(value)
        if self.head is None:
            self.head = node
            return
        
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = node

    def remove_node(self, target_node_data):
        if self.head.value == target_node_data:
            self.head = self.head.next_node
            return

        previous_node = self.head
        for node in self:
            if node.value == target_node_data:
                previous_node.next_node = node.next_node
                return
            previous_node = node

    def printLinkedList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value,"->", end=" ")
            current_node = current_node.next_node
        print('None')

values = [1, 31, 7, 1]
l_list = LinkedList()
for value in values:
    l_list.append_node(value)
l_list.printLinkedList()



