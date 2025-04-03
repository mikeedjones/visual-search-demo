import json
from io import BytesIO

import requests
import streamlit as st
from PIL import Image


def display_product_card(json_data):
    """Display a product in a nicely formatted card layout."""
    # Parse JSON if it's a string
    if isinstance(json_data, str):
        try:
            product = json.loads(json_data)
        except json.JSONDecodeError:
            st.error("Invalid JSON data")
            return
    else:
        product = json_data

    # Create a two-column layout
    col1, col2 = st.columns([1, 2])

    with col1:
        # Display the product image
        image_url = product.get("ImageUrl", "")
        if image_url:
            response = requests.get(image_url, timeout=3)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                st.image(img, use_container_width=True)
            else:
                st.warning("Image could not be loaded")
        else:
            st.warning("No image available")

        # Price and CTA
        st.markdown(f"### £{product.get('Price', 'N/A'):.2f}")
        st.link_button("View Product", product.get("ProductUrl", "#"))

    with col2:
        # Product title and brand
        st.markdown(f"## {product.get('ProductName', 'Product Name')}")
        st.markdown(f"*by {product.get('Brand', 'Brand')}*")

        # Product description
        st.markdown("**Description:**")
        st.markdown(product.get("SkuProductDescription", "No description available"))

        # Features - Convert string to list and display as bullets
        if product.get("Features"):
            features = product.get("Features").split(", ")
            st.markdown("**Features:**")
            for feature in features:
                st.markdown(f"- {feature}")
