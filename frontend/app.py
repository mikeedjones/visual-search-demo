import json

import requests
import streamlit as st
from PIL import Image

from product_card import display_product_card

# Set page config
st.set_page_config(page_title="Visual Product Search", page_icon="🔍", layout="wide")

api_url = "http://localhost:8000"

# Main content
st.title("🔍 Visual Product Search")
st.write("Upload an image to find similar products in our catalog.")

with open("products.json", "r", encoding="utf-8") as fp:
    products = json.load(fp)

products = {product["ProductID"]: product for product in products}

uploaded_file = None
camera_image = None

col1, col2 = st.columns(2)

with col1:
    # File uploader
    tab1, tab2 = st.tabs(["Upload Image", "Use Camera"])
    with tab1:
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True)

    # Tab 2: Camera Input
    with tab2:
        enable = st.checkbox("Enable camera")
        camera_image = st.camera_input("Take a picture", disabled=not enable, kwargs={"height": 200})

    if not uploaded_file and not camera_image:
        st.info("Please upload an image or enable the camera.")

with col2:
    # Search on upload
    if uploaded_file or camera_image:
        image = camera_image if camera_image else uploaded_file
        try:
            with st.spinner("Searching for similar products..."):
                # Reset file position before sending
                uploaded_file.seek(0)

                # Send the image to the FastAPI service
                files = {"query_image": image}
                response = requests.post(f"{api_url}/visual-search", files=files, timeout=3)

                if response.status_code == 200:
                    result = response.json()

                    # Display the results
                    with col2:
                        st.subheader("Search Results")
                        st.success("Match found!")
                        display_product_card(products[result["best_match_id"]])

                else:
                    st.error(f"Error: {response.status_code}")
                    st.code(response.text)

        except requests.exceptions.ConnectionError:
            st.error(f"Could not connect to the API at {api_url}. Is the server running?")
