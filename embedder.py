
from functools import partial

import torch
from PIL import Image
from transformers import AutoImageProcessor, Dinov2Model


def embed_image(image: Image.Image, image_processor: AutoImageProcessor, model: Dinov2Model) -> torch.Tensor:
    inputs = image_processor(image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    return outputs.pooler_output


def load_embedder():
    image_processor = AutoImageProcessor.from_pretrained("facebook/dinov2-base")
    model = Dinov2Model.from_pretrained("facebook/dinov2-base")

    return partial(embed_image, image_processor=image_processor, model=model)
