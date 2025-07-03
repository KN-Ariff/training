import streamlit as st
import cv2
import joblib
from PIL import Image
import numpy as np

st.image("pp.jpg")
st.title("PineApple with AI")
st.text("Cracked Pineapple :sad: Detector with KNN")

model = joblib.load("trained_model_KNN.pkl")

# Preprocessing and feature extraction
def preprocess_image(img):
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    return edges
 
def extract_features(img):
    resized = cv2.resize(img, (64, 64))
    return resized.flatten().reshape(1, -1)

uploaded_file = st.file_uploader("Pineapple Note: Where your picture at?", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L") #convert to grayscale
    img_array = np.array(image)

    st.image(image, caption="Pineapple Note: Image succesfully uploaded.")

    processsed_image = preprocess_image(img_array)
    features = extract_features(processsed_image)

    prediction = model.predict(features)[0]
    label = "HECK Yeah!!" if prediction == 1 else "Aww. Spolied!!!"
    st.success(f"**Prediction:** {label}")
