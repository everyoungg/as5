
import heapq

class Heap:
    def __init__(self):
        self._data = []

    def push(self, item):
        heapq.heappush(self._data, item)

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self._data)
        return None

    def peek(self):
        if not self.is_empty():
            return self._data[0]
        return None

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
