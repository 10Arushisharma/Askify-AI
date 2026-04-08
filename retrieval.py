def retrieve_docs(db, query):
    return db.similarity_search(query, k=5)