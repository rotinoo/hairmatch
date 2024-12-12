import streamlit as st

# Centered logo with adjustable size
logo_url = "https://storage.googleapis.com/hairmatch-frontend-asset/assets/black-logo.png"
logo_size = 300  # You can change this value to adjust the size

st.logo("https://storage.googleapis.com/hairmatch-frontend-asset/assets/black-logo.png")

st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="{logo_url}" width="{logo_size}">
    </div>
    """,
    unsafe_allow_html=True
)

# Title and introduction with adjustable font sizes
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;

    }
    .subheader {
        font-size: 24px;
    }
    .description {
        font-size: 20px;
        margin-bottom:20px;
    }
    .list {
        font-size: 20px;
        margin-bottom:10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">Welcome to HairMatch!</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Discover Your Perfect Look</div>', unsafe_allow_html=True)

# Description of HairMatch
st.markdown(
    """
    <div class="description" ;">
    HairMatch is your ultimate companion for exploring hairstyles that suit you best. Due to certain limitations, we are currently focusing on men's hairstyles. However, we are planning to expand to women's hairstyles soon.  Using advanced facial and hair type recognition, we recommend hairstyles tailored to your unique features. Whether you're looking for a fresh new look or just some inspiration, HairMatch is here to help you make the right choice. 🌟
    </div>
    <div class="list">Why Choose HairMatch?</div>
    <div class="list">- Personalized hairstyle recommendations based on your face and hair type.</div>
    <div class="list">- Easy-to-use interface that lets you upload or capture photos.</div>
    <div class="list">- Explore a variety of styles to find your perfect match.</div>
    
    <div class="description" ;">
    Ready to transform your style? Get started now! Go to the Hairstyle Recommendation page in the sidebar.</div>
    
    """,
    unsafe_allow_html=True
)
