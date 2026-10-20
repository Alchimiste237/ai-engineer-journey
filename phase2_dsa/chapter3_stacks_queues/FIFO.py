from collections import deque

class Queue:

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"Queue ( front -> { list(self._data) } ) "
    # pass

queue = Queue()
queue.enqueue(15)
queue.enqueue(17)
queue.enqueue(20)
queue.enqueue(45)
queue.dequeue()
print(queue)
