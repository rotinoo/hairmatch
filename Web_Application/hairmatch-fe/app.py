import streamlit as st
import cv2
import numpy as np
from PIL import Image
import requests

# Backend API URL
BASE_URL = "http://localhost:8080"

# Title and Subheader
st.title("Hair Style Recommendation")
st.subheader("Discover the best hairstyle for you!")

# Option to upload or use camera
option = st.radio("Choose how to provide your image:", ("Upload an Image", "Use Camera"))

# Placeholder for the image
image = None

if option == "Upload an Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
elif option == "Use Camera":
    captured_image = st.camera_input("Capture an image using your webcam")
    if captured_image is not None:
        image = Image.open(captured_image)

# If an image is provided
if image is not None:
    # Save the image to disk temporarily
    image_path = "temp_image.jpg"
    image.save(image_path)

    # Analyze button
    if st.button("Analyze My Hairstyle"):
        st.info("Processing... Please wait.")

        # Step 1: Detect Face Type
        try:
            with open(image_path, "rb") as img_file:
                face_response = requests.post(f"{BASE_URL}/api/detect/face", files={"image": img_file})
            face_response.raise_for_status()  # Raise error for non-200 responses
            face_data = face_response.json()
            face_type = face_data.get("tipe_wajah", "Unknown")
            st.write(f"Detected Face Type: **{face_type}**")
        except Exception as e:
            st.error(f"Error detecting face type: {e}")
            face_type = "Unknown"

        # Step 2: Detect Hair Type
        try:
            with open(image_path, "rb") as img_file:
                hair_response = requests.post(f"{BASE_URL}/api/detect/hair", files={"image": img_file})
            hair_response.raise_for_status()
            hair_data = hair_response.json()
            hair_type = hair_data.get("tipe_rambut", "Unknown")
            st.write(f"Detected Hair Type: **{hair_type}**")
        except Exception as e:
            st.error(f"Error detecting hair type: {e}")
            hair_type = "Unknown"

        # Step 3: Fetch Recommendations
        if face_type != "Unknown" and hair_type != "Unknown":
            try:
                recommend_response = requests.post(
                    f"{BASE_URL}/api/recommend",
                    json={"tipe_wajah": face_type, "tipe_rambut": hair_type}
                )
                recommend_response.raise_for_status()
                recommend_data = recommend_response.json()
                recommendations = recommend_data.get("gaya_rambut", [])
                st.write("Recommended Hairstyles:")
                for style in recommendations:
                    st.image(style["gambar"], caption=style["nama"], use_column_width=True)
            except Exception as e:
                st.error(f"Error fetching recommendations: {e}")
