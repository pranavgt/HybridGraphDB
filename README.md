# HybridGraphDB: Multi-Model Query Routing with HNSW Acceleration

## Overview
HybridGraphDB demonstrates how Hierarchical Navigable Small World (HNSW) graphs can optimize query routing across multi-model databases (SQL, graph, document, vector). It uses HNSW for fast approximate nearest neighbor search to route queries efficiently, minimizing overhead and enhancing privacy for AI-driven applications.

## Features
- **HNSW-Powered Search**: Uses `hnswlib` for indexing hybrid data vectors.
- **Multi-Model Query Routing**: Routes to SQL, graph, or document stores based on proximity.
- **Hybrid Embeddings**: Encodes multi-model data into a shared vector space.
- **Efficient Joins**: Avoids costly relational joins using graph distances.
- **Local-First**: Supports lightweight, privacy-aware querying for AGI/LLM tasks.

## Prerequisites
- Python 3.8+
- Java 11+ (for ArcadeDB)
- PyCharm (or any IDE)
- Git

## Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd HybridGraphDB
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install ArcadeDB**:
   - Download ArcadeDB from [arcadedb.com](https://arcadedb.com/).
   - Start the server:
     ```bash
     ./arcadedb/bin/server.sh  # On Windows: arcadedb\bin\server.bat
     ```
   - Verify at `http://localhost:2480`.

5. **Run the Application**:
   ```bash
   uvicorn query_router:app --reload
   ```
   Access the API at `http://localhost:8000`.

6. **Run the Demo UI** (optional):
   ```bash
   streamlit run demo/app.py
   ```

## Project Structure
```
HybridGraphDB/
├── engine/                # HNSW and routing logic
├── dataloaders/          # Data ingestion scripts
├── adapters/             # SQL, graph, document connectors
├── benchmarks/           # Performance comparison scripts
├── demo/                 # Streamlit demo UI
├── docs/                 # Documentation and diagrams
├── query_router.py       # Main query routing engine
├── requirements.txt       # Dependencies
├── README.md             # Project overview
└── .gitignore            # Git ignore rules
```

## Demo Use Case
Find customers within 2 hops of a flagged transaction with logs and patterns resembling known fraud cases, combining graph traversal, embedding similarity, SQL joins, and time-based filtering.

## Future Work
- Docker microservices
- Real-time index updates
- Private LLM integration

## References
- Malkov, Yu. A., & Yashunin, D. A. (2016). [Efficient and robust approximate nearest neighbor search using HNSW](https://arxiv.org/abs/1603.09320)
- [ArcadeDB](https://arcadedb.com/)
- [hnswlib](https://github.com/nmslib/hnswlib)