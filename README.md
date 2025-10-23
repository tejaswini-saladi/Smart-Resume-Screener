# 🧠 Smart Resume Screener

## 📄 Description
**Smart Resume Screener** is an AI-powered web application that automatically classifies resumes into relevant job categories using **Natural Language Processing (NLP)** and **Machine Learning**.  
It simplifies hiring by analyzing resumes and categorizing them into domains such as **Data Science**, **Java Developer**, **HR**, **Business Analyst**, **Web Developer**, and more.

---
## Project Overview

The **Smart Resume Screener** simplifies hiring by automatically analyzing resumes and classifying them into predefined job categories such as:
- Data Science  
- Java Developer  
- HR  
- Business Analyst  
- Web Developer, and more.

This saves recruiters time and ensures efficient candidate shortlisting.

---
## ⚙️ Key Features
- 🧹 **Text Cleaning:** Removes punctuation, stopwords, and performs lemmatization using NLTK.  
- 🔤 **Feature Extraction:** Implemented both **TF-IDF vectorization** and **Word2Vec embeddings** for feature representation.  
- 🧠 **Model Training:** Trained using `KNeighborsClassifier` wrapped in a `OneVsRestClassifier`.  
- 📊 **Evaluation:** Measured using Accuracy, Precision, Recall, and F1-score.  
- 💻 **Interactive Web App:** Built with Streamlit for instant, user-friendly predictions.

---

## 🧰 Technologies Used
- **Python**
- **Scikit-learn**
- **NLTK**
- **Pandas**
- **NumPy**
- **Streamlit**
- **Pickle**

---

## 📈 Model Performance Comparison

| **Metric**        | **TF-IDF** | **Word2Vec** |
|--------------------|------------|--------------|
| **Train Accuracy** | 0.9883     | 0.9467       |
| **Test Accuracy**  | 0.9845     | 0.8497       |
| **Precision (avg)**| 0.98       | 0.88         |
| **Recall (avg)**   | 0.97       | 0.85         |
| **F1-Score (avg)** | 0.97       | 0.84         |

---

## 🧠 Model Insights
- Both **TF-IDF** and **Word2Vec** embeddings provided strong classification performance across multiple job domains.  
- A **confusion matrix visualization** was generated to analyze model predictions and performance.

---

## 🖥️ Application Access
To run the application locally with Streamlit, use the following command:http://localhost:8504/



