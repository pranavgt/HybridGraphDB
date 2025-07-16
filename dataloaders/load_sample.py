import numpy as np
from engine.hnsw_router import HNSWRouter

router = HNSWRouter(dim=128)
sample_vectors = np.random.rand(10, 128).astype(np.float32)
sample_labels = [f'sql_{i}' if i % 2 == 0 else f'graph_{i}' for i in range(10)]

router.add_data(sample_vectors, sample_labels)
