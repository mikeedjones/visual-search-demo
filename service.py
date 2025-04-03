import json

import torch
import uvicorn
from fastapi import FastAPI, UploadFile
from PIL import Image

from embedder import load_embedder


def build_server():
    app = FastAPI()
    embedder = load_embedder()
    product_embeddings = torch.load("index/embeddings.pt")
    with open("index/product_ids.json", "r", encoding="utf-8") as fp:
        product_ids = json.load(fp)


    @app.get("/")
    def read_root():
        return {"message": "Welcome to the Visual Product Search API"}

    @app.post("/visual-search")
    def visual_search(query_image: UploadFile):
        # Read the image file
        image = Image.open(query_image.file)

        # Embed the image
        query_embedding = embedder(image)

        # Calculate the similarity
        similarities = torch.cosine_similarity(query_embedding, product_embeddings)
        best_match_index = torch.argmax(similarities).item()
        best_match_id = product_ids[best_match_index]

        return {"best_match_id": best_match_id}

    return app

if __name__ == "__main__":
    # Start the FastAPI server
    uvicorn.run(build_server())
