from fastapi import FastAPI, Query
import numpy as np

from engine.hnsw_router import HNSWRouter
from adapters.sql_adapter import SQLAdapter
from adapters.arcadedb_adapter import ArcadeDBAdapter

app = FastAPI()

# Example setup
router = HNSWRouter(dim=128)
sql_adapter = SQLAdapter()
graph_adapter = ArcadeDBAdapter()

@app.post("/route_query")
def route_query(vector: list = Query(...)):
    np_vector = np.array(vector).astype(np.float32)
    labels, distances = router.query(np_vector)
    # Example: route based on label prefix
    results = {}
    for label in labels:
        if label.startswith("sql_"):
            results[label] = sql_adapter.run_query("SELECT * FROM table WHERE id=1")
        elif label.startswith("graph_"):
            results[label] = graph_adapter.run_query("MATCH (n) RETURN n LIMIT 1")
        else:
            results[label] = "Unknown route"
    return {"results": results}
