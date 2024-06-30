from langchain.document_loaders import UnstructuredURLLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
import google.generativeai as palm
from .embeddings import generate_embeddings
import faiss
import numpy as np

palm.configure(api_key='AIzaSyCFPXxgS8Stxq975EZSM9Rn71Q5naJXHqs')

# FAISS index and database
dimension = 768  # Assuming the embedding size is 768
index = faiss.IndexFlatL2(dimension)
url_database = {}

def create_vector_index(urls):
    loader = UnstructuredURLLoader(urls=urls)
    index = VectorstoreIndexCreator(
        embedding=GooglePalmEmbeddings(google_api_key='AIzaSyCFPXxgS8Stxq975EZSM9Rn71Q5naJXHqs'),
        text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    ).from_loaders([loader])
    return index

def update_vector_database(url, embeddings):
    global index, url_database
    index.add(np.array(embeddings))
    url_database[len(url_database)] = url

def query_vector_database(user_query, previous_context):
    global index, url_database
    query_embedding = generate_embeddings(user_query + " " + previous_context)
    D, I = index.search(np.array(query_embedding), 1)  # Search for the closest vector
    nearest_url = url_database[I[0][0]]
    return nearest_url
