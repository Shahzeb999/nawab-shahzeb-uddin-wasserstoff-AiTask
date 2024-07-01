import google.generativeai as palm

palm.configure(api_key='AIzaSyCFPXxgS8Stxq975EZSM9Rn71Q5naJXHqs')

def generate_embeddings(text):
    model = "models/embedding-gecko-001"
    embeddings = palm.generate_embeddings(model=model, text=x)
    return embeddings['embedding']

    