"""
Pipeline to build a vector database of product images from diy.com.

Get product images from diy.com, embed them using a pre-trained model, and
save the embedded images to a local vector database.
"""

import io
import json

import requests
import torch
from PIL import Image
from tqdm import tqdm

from embedder import load_embedder


def build_index(product_files:str):
    with open(product_files, "r", encoding="utf-8") as fp:
        products = json.load(fp)

    # Load the embedder
    embedder = load_embedder()

    product_embeddings = []
    product_ids = []

    for row in tqdm(products):
        product_ids.append(row["ProductID"])
        image_url = row["ImageUrl"]
        # Download the image
        image = Image.open(io.BytesIO(requests.get(image_url).content))
        # Embed the image
        product_embeddings.append(embedder(image))

    # Save the embeddings to a file
    torch.save(torch.cat(product_embeddings), "index/embeddings.pt")

    # Save the product IDs to a file
    with open("index/product_ids.json", "w", encoding="utf-8") as fp:
        json.dump(product_ids, fp)


if __name__ == "__main__":
    build_index("products.json")