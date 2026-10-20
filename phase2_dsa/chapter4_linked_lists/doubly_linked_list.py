class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None   # ← the addition

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None   # track tail for O(1) append AND prepend

    def append(self, data):
        """Add to end. O(1) because we track tail."""
        new_node = DoublyNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Add to front. O(1)."""
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_node(self, node):
        """
        Delete a specific node in O(1) — given the node itself,
        not a value. This is the key advantage over singly linked list.
        Used directly in LRU Cache implementation.
        """
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next   # deleting head

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev   # deleting tail

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " ↔ ".join(result) + " None"
