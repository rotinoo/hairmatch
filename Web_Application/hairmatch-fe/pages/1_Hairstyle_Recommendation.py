import streamlit as st
from utils.api_client import detect_face_type, detect_hair_type, fetch_recommendations
from PIL import Image

logo = "https://storage.googleapis.com/hairmatch-frontend-asset/assets/black-logo.png"

st.logo(logo)

def app():
    st.title("HairMatch")
    st.subheader("Your Perfect Style, Matched to You!")

    # Image Input Options
    option = st.radio("Choose how to provide your image:", ("Upload an Image", "Use Camera"))
    image = None

    if option == "Upload an Image":
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", width=200)
    elif option == "Use Camera":
        captured_image = st.camera_input("Capture an image using your webcam")
        if captured_image:
            image = Image.open(captured_image)

    if image:
        if st.button("Analyze My Hairstyle"):
            st.info("Processing...")

            # Detect face and hair types
            face_type = detect_face_type(image)
            hair_type = detect_hair_type(image)

            if face_type and hair_type:
                st.success(f"##### Detected Face Type: **{face_type}**")
                st.success(f"##### Detected Hair Type: **{hair_type}**")

                # Fetch recommendations directly from the API
                recommendations = fetch_recommendations(face_type, hair_type, "image_list.csv")

                if recommendations:
                    st.write("### Recommended Hairstyles:")

                    for rec in recommendations:
                        st.write(f"#### {rec['name']}")
                        st.write(f"##### {rec['description']}")  # Directly display the description

                        # (Optional) Handle image URLs if included in API
                        if rec["urls"]:
                            carousel_html = """
                            <div class="carousel" style="display: flex; overflow-x: scroll; gap: 10px; justify-content: center;">
                            """
                            for url in rec["urls"]:
                                carousel_html += f'<img src="{url}" alt="Hairstyle" style="height: 300px; border-radius: 20px;">'
                            carousel_html += "</div>"

                            st.markdown(carousel_html, unsafe_allow_html=True)
                else:
                    st.error("No recommendations found. Check the log for more details.")

            else:
                st.error("Could not detect face or hair type.")

app()
