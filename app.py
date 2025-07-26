# app.py

import streamlit as st
from PIL import Image
from utils import preprocess_image, load_model, predict, speak

# Page config
st.set_page_config(
    page_title="Smart Waste Classifier",
    layout="wide",
)

# Optional: hide footer/menu for cleaner UI
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Title
st.title("♻️ Smart Waste Classifier")
st.caption("Classify waste as biodegradable, recyclable, or non-recyclable using AI")

# Input method
option = st.radio("Choose Input Method", ["Upload Image", "Use Camera"], horizontal=True)

img = None
if option == "Upload Image":
    uploaded = st.file_uploader("Upload an image of the waste", type=["jpg", "jpeg", "png"])
    if uploaded:
        img = Image.open(uploaded).convert("RGB")
        st.image(img, caption="Uploaded Image", use_container_width=True)

else:
    camera_img = st.camera_input("Take a picture")
    if camera_img:
        img = Image.open(camera_img).convert("RGB")
        st.image(img, caption="Camera Image", use_container_width=True)

# Load model
model = load_model()

# Prediction UI
if img:
    col1, col2, col3 = st.columns([1, 2, 1])  # center-align button
    with col2:
        if st.button("🔍 Classify Waste", use_container_width=True):
            with st.spinner("Classifying..."):
                tensor = preprocess_image(img)
                label = predict(model, tensor)

            st.success(f"🧠 Prediction: **{label.capitalize()} Waste**")
            audio_file = speak(f"This is {label} waste.")
            st.audio(audio_file, format="audio/mp3")
