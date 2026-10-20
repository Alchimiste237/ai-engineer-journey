class Stack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)


    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __str__(self):
        return f"Stack ( top -> { self._data[::-1] } )"

stack = Stack()
stack.push(12)
stack.push(120)
stack.push(102)
stack.push(121)
# print(stack.size())
