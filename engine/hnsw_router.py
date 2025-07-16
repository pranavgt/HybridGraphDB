import hnswlib

class HNSWRouter:
    def __init__(self, dim=128, max_elements=10000, ef=200, M=16):
        self.p = hnswlib.Index(space='cosine', dim=dim)
        self.p.init_index(max_elements=max_elements, ef_construction=ef, M=M)
        self.p.set_ef(ef)
        self.labels = {}

    def add_data(self, vectors, labels):
        self.p.add_items(vectors, labels)
        for i, label in enumerate(labels):
            self.labels[label] = vectors[i]

    def query(self, vector, k=5):
        labels, distances = self.p.knn_query(vector, k=k)
        return labels[0], distances[0]
