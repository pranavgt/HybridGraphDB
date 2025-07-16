import hnswlib
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample data (replace with your data from ArcadeDB)
data = ["Customer John Doe", "Transaction: flagged fraud", "Log: suspicious activity"]
embeddings = model.encode(data)  # Shape: (3, 384)

# Initialize HNSW index
dim = embeddings.shape[1]  # 384 for MiniLM
index = hnswlib.Index(space='cosine', dim=dim)
index.init_index(max_elements=10000, ef_construction=200, M=16)

# Add embeddings
index.add_items(embeddings, ids=np.arange(len(data)))

# Test query
query = model.encode(["Fraud-like transaction"])
labels, distances = index.knn_query(query, k=2)
print("Nearest neighbors:", [data[i] for i in labels[0]])