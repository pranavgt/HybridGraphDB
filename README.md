<h1 align="center">HybridGraphDB: Multi-Model Query Routing with HNSW Acceleration</h1>

<div align="center">
  <img src="assets/hybridgraphdb.png" alt="HybridGraphDB Architecture Diagram" width="80%"/>
</div>

<br/>

<table>
  <tr>
    <td valign="top" width="60%">

### 🧠 Overview
HybridGraphDB demonstrates how Hierarchical Navigable Small World (HNSW) graphs can optimize query routing across multi-model databases (SQL, graph, document, vector etc.).  
It uses HNSW for fast approximate nearest neighbor search to route queries efficiently, minimizing overhead and enhancing privacy for AI-driven applications.

### 🚀 Features
- **HNSW-Powered Search**: Uses `hnswlib` for indexing hybrid data vectors.  
- **Multi-Model Query Routing**: Routes to SQL, graph, or document stores based on proximity.  
- **Hybrid Embeddings**: Encodes multi-model data into a shared vector space.  
- **Efficient Joins**: Avoids costly relational joins using graph distances.  
- **Local-First**: Supports lightweight, privacy-aware querying for AGI/LLM tasks.  

</td>
<td width="40%" align="center">

<img src="assets/hybridgraphdb.png" alt="HybridGraphDB Architecture" width="100%"/>

</td>
</tr>
</table>

---

## 🛠️ Prerequisites
- Python 3.8+  
- Java 11+ (for ArcadeDB)  
- PyCharm (or any IDE)  
- Git  

## ⚙️ Setup
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd HybridGraphDB
