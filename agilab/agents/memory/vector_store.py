# Tiny in-memory vector store placeholder
class VectorStore:
    def __init__(self, dim=384): self.data = []; self.dim = dim
    def add(self, vec, meta): self.data.append((vec, meta))
    def search(self, vec, topk=5): return self.data[:topk]
