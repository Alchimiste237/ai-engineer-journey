from collections import deque
import time

class TaskQueue:
    def __init__(self):
        self._queue = deque()
        self._completed = []

    def add_task(self, task_name, priority=False):
        """Add task. Priority tasks jump to the front."""
        if priority:
            self._queue.appendleft(task_name)  # jump the line
        else:
            self._queue.append(task_name)       # normal queue

    def process_next(self):
        """Process the next task in queue."""
        if not self._queue:
            return "No tasks in queue"
        task = self._queue.popleft()
        self._completed.append(task)
        return f"Processed: {task}"

    def process_all(self):
        """Process all tasks in order."""
        while self._queue:
            print(self.process_next())

    def status(self):
        print(f"Pending:   {list(self._queue)}")
        print(f"Completed: {self._completed}")


# Simulate an ML pipeline task queue
pipeline = TaskQueue()
pipeline.add_task("Load dataset")
pipeline.add_task("Preprocess data")
pipeline.add_task("Train model")
pipeline.add_task("Validate model")
pipeline.add_task("URGENT: Fix data corruption", priority=True)

pipeline.status()
print("---")
pipeline.process_all()
print("---")
pipeline.status()
