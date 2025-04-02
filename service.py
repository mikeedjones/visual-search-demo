import io
import json

import torch
from fastapi import FastAPI, UploadFile
from PIL import Image
from uvicorn import run

from embedder import load_embedder


def build_app():
    app = FastAPI()
    embedder = load_embedder()
    index = torch.load("index/embeddings.pt")
    with open("index/products_ids.json", "r", encoding="utf-8") as fp:
        product_ids = json.load(fp)

    @app.post("/visual-search")
    async def search_products(query_image: UploadFile):

        embedding = embedder(Image.open(io.BytesIO(query_image.file.read())).convert("RGB"))

        similarities = torch.cosine_similarity(embedding, index, dim=1)
        best_match_index = similarities.argmax()
        best_match_id = product_ids[int(best_match_index)]

        return {"best_match_id": best_match_id}

    return app


if __name__ == "__main__":
    run(build_app())
