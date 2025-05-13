# 🎭 Sentiment Analysis on Movie Reviews

This project is a deep learning-based sentiment analysis tool that classifies movie reviews as **positive** or **negative**. Built using Python, Keras (TensorFlow backend), and Streamlit for the interactive frontend.

---

## 📌 Project Description

This app uses a pre-trained LSTM (Long Short-Term Memory) neural network to detect the sentiment of a movie review. Users can input any review, and the model will predict whether it's positive or negative.

The dataset used is the **IMDB Dataset of 50K Movie Reviews**, obtained via the Kaggle API.

---

## 🚀 Features

- Interactive web UI built with Streamlit
- Trained LSTM model for sentiment prediction
- Live prediction of user input reviews
- Preprocessing using Keras Tokenizer and Padding
- Easily deployable on Streamlit Cloud

---

## 🧠 Tech Stack

- Python 3
- TensorFlow / Keras
- Pandas
- Scikit-learn
- Streamlit
- IMDB Dataset (via Kaggle)

---

## 📂 Folder Structure
<pre> 📁 Project Root 
  ├── app.py # Main Streamlit app 
  ├── sentiment_model.h5 # Trained LSTM model 
  ├── tokenizer.pickle # Fitted tokenizer for preprocessing 
  ├── README.md 
  └── requirements.txt # Python dependencies 
</pre>

---

## 📥 Installation & Running Locally

```bash
git clone https://github.com/SUJAY-HK/Sentiment-Analysis-Streamlit.git
cd  Sentiment-Analysis-Streamlit

# (optional) create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🧪 How It Works

- The user enters a **movie review** through the Streamlit web app.
- The input text is:
  - **Tokenized** using a fitted tokenizer
  - **Padded** to a fixed sequence length
- The processed text is fed into a **trained LSTM model**.
- The model outputs a **probability score**.
- This score is mapped to:
  - **Positive** sentiment (if probability > 0.5)
  - **Negative** sentiment (if probability ≤ 0.5)

---

## 🔗 Dataset

- The model was trained on the **IMDB Dataset of 50K Movie Reviews**.
- Source: [Kaggle - IMDB Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)






