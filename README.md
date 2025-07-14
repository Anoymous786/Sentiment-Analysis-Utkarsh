# 🎭 Sentiment Analysis on Movie Reviews

**Sentiment Analysis** is a web-based deep learning application developed by **Utkarsh Singh** that classifies movie reviews as **Positive** or **Negative** using a trained **LSTM model** and an interactive **Streamlit UI**.

This project demonstrates the power of Natural Language Processing (NLP) and Recurrent Neural Networks (RNNs) for text classification tasks.

---

## 🚀 Live Demo

🌐 [Try the App Live](https://sentimental-review.streamlit.app)

---

## ✨ Features

- 📝 Input any custom movie review and get real-time sentiment prediction
- 🧠 Trained LSTM (Long Short-Term Memory) model for sequence analysis
- 🔄 Preprocessing includes tokenization, padding, and embedding
- 🎛️ Clean UI with **Streamlit** for interactive experience
- 📊 Trained on **50,000 IMDB Reviews** from Kaggle for robust accuracy

---

## 💻 Technologies Used

| Layer         | Tools / Libraries                           |
|---------------|----------------------------------------------|
| Frontend/UI   | Streamlit                                    |
| Backend       | Python 3, Flask (optional)                   |
| ML/NLP        | TensorFlow, Keras, NLTK, Scikit-learn        |
| Preprocessing | Tokenizer, Padding, LSTM, Dense Layers       |
| Deployment    | Streamlit Cloud                              |
| Dataset       | IMDB Movie Reviews (via Kaggle)              |

---

## 📂 Project Structure

```
Sentiment-Analysis-Streamlit/
├── app.py                 # Streamlit UI entry point
├── sentiment_model.h5    # Trained LSTM model file
├── tokenizer.pickle      # Tokenizer object for preprocessing
├── requirements.txt      # Python package dependencies
└── README.md
```

---

## 🚀 Getting Started Locally

### 🔧 Clone & Setup
```bash
git clone https://github.com/Anoymous786/Sentiment-Analysis-Utkarsh.git
cd Sentiment-Analysis-Utkarsh
```

### 📦 Install Requirements
```bash
pip install -r requirements.txt
```

### ▶️ Run the App
```bash
streamlit run app.py
```

App will run at: [http://localhost:8501](http://localhost:8501)

---

## ✍️ Author

**Utkarsh Singh**  
GitHub: [Anoymous786](https://github.com/Anoymous786)  
Email: [utsi22ise@cmrit.ac.in](mailto:utsi22ise@cmrit.ac.in)  
LinkedIn: [linkedin.com/in/utkarsh746](https://linkedin.com/in/utkarsh746)

---

> ✅ Built by Utkarsh Singh as part of a machine learning and full-stack portfolio to demonstrate LSTM-based sentiment classification and Python UI development.
