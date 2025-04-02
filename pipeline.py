"""
Pipeline to build a vector database of product images from diy.com.

Get product images from diy.com, embed them using a pre-trained model, and
save the embedded images to a local vector database.
"""

import io
import json

import pandas as pd
import requests
import torch
from PIL import Image
from tqdm import tqdm

from embedder import load_embedder


def build_index(product_file: str):
    embedder = load_embedder()

    products_df = pd.read_json(product_file)

    embeddings = []

    for _, row in tqdm(products_df.iterrows()):
        # download the image
        response = requests.get(row["ImageUrl"], timeout=10)
        response.raise_for_status()

        # open the image
        image = Image.open(io.BytesIO(response.content)).convert("RGB")

        # embed the image
        embeddings.append(embedder(image))

    torch.save(torch.cat(embeddings), "index/embeddings.pt")
    with open("index/products_ids.json", "w", encoding="utf-8") as fp:
        json.dump(products_df["ProductID"].tolist(), fp)

if __name__ == "__main__":
    build_index("products.json")