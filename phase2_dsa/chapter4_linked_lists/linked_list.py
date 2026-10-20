class Node:
    """A single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None   # pointer to the next node

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    """Singly linked list implementation."""

    def __init__(self):
        self.head = None   # empty list starts with no head
        self._size = 0

    # ── Insertion ──────────────────────────────────────────

    def append(self, data):
        """Add node at the end. O(n) — must traverse to tail."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next   # walk to the end
            current.next = new_node
        self._size += 1

    def prepend(self, data):
        """Add node at the beginning. O(1) — just redirect head."""
        new_node = Node(data)
        new_node.next = self.head   # new node points to old head
        self.head = new_node        # head now points to new node
        self._size += 1

    def insert_after(self, target_data, new_data):
        """Insert new node after a node containing target_data."""
        current = self.head
        while current is not None:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next   # new node points forward
                current.next = new_node        # previous node points to new
                self._size += 1
                return
            current = current.next
        raise ValueError(f"{target_data} not found in list")

    # ── Deletion ───────────────────────────────────────────

    def delete(self, data):
        """Remove first node containing data. O(n)."""
        if self.head is None:
            raise ValueError("Cannot delete from empty list")

        # Special case: deleting the head
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return

        # General case: find the node BEFORE the one to delete
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next   # skip over the node
                self._size -= 1
                return
            current = current.next

        raise ValueError(f"{data} not found in list")

    # ── Search & Access ────────────────────────────────────

    def search(self, data):
        """Return True if data exists in list. O(n)."""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def get(self, index):
        """Return data at index. O(n)."""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    # ── Utility ────────────────────────────────────────────

    def to_list(self):
        """Convert to Python list for easy testing/comparison."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        return self._size

    def __str__(self):
        nodes = self.to_list()
        return " → ".join(str(n) for n in nodes) + " → None"


# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
print(ll)             # 5 → 10 → 20 → 30 → None
ll.insert_after(10, 15)
print(ll)             # 5 → 10 → 15 → 20 → 30 → None
ll.delete(15)
print(ll)             # 5 → 10 → 20 → 30 → None
print(ll.get(2))      # 20
print(len(ll))        # 4
