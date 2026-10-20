"""
Using your LinkedList class, create a list
using append(), print it, then delete node 3 and print again.

"""
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
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        current = self.head
        if self.head.data == data:
            self.head = current.next
            return
        else:
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                current = current.next
        print(f"No node containing {data} found ")

    def display(self):
        current = self.head
        print(current.data)
        while current.next:
            current = current.next
            print(current.data)

ll = LinkedList()
ll.append(5)
ll.append(8)
ll.append(15)
ll.append(18)
ll.append(25)
ll.display()
ll.delete(15)
ll.display()
