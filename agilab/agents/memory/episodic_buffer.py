from collections import deque
class EpisodicBuffer:
    def __init__(self, max_items=200): self.buf = deque(maxlen=max_items)
    def add(self, item): self.buf.append(item)
    def recent(self, k=10): return list(self.buf)[-k:]
