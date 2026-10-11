class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

# --- now USE it ---
ll = LinkedList()
ll.append(10)
ll.append(25)
ll.append(7)
ll.append(42)
ll.print_list()