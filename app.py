
import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model and tokenizer
@st.cache_resource
def load_model_and_tokenizer():
    model = load_model('sentiment_model.h5')
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    return model, tokenizer

model, tokenizer = load_model_and_tokenizer()

# Prediction function
def predict_sentiment(review):
    sequence = tokenizer.texts_to_sequences([review])
    padded = pad_sequences(sequence, maxlen=200)
    prediction = model.predict(padded)[0][0]
    return "Positive 😊" if prediction > 0.5 else "Negative 😞"

# UI
st.title("🎬 Movie Review Sentiment Analyzer")
st.write("Enter a movie review below to analyze its sentiment.")

user_input = st.text_area("Your Review:", height=150)

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        sentiment = predict_sentiment(user_input)
        st.success(f"Sentiment: {sentiment}")
