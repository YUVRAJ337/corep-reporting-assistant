from chromadb import Client
from sentence_transformers import SentenceTransformer
from pathlib import Path

# Load embedding model (runs locally, free)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB client (NEW API – no persist_directory here)
client = Client()

# Create / get collection
collection = client.get_or_create_collection(name="pra_rules")


def load_rules_into_db():
    """
    Load PRA rules from text file, split into chunks,
    embed them, and store in ChromaDB.
    """
    rules_path = Path("../data/rules/pra_rules.txt")
    text = rules_path.read_text()

    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    embeddings = embedding_model.encode(chunks)


    for idx, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            embeddings=[embeddings[idx].tolist()],
            ids=[f"rule_{idx}"]
        )


def retrieve_relevant_rules(question, k=3):
    """
    Retrieve top-k relevant rule chunks using semantic search.
    """
    query_embedding = embedding_model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k
    )

    return results["documents"][0]
