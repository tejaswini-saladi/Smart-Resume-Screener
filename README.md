# Smart Resume Screener

**Smart Resume Screener** is an **AI-powered web application** that automatically classifies resumes into relevant job categories using **Natural Language Processing (NLP)** and **Machine Learning**.  
It uses **TF-IDF vectorization** and a trained **KNeighborsClassifier** model to predict the job domain from resume text.

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

-  **Text Cleaning:** Removes punctuation, stopwords, and performs lemmatization using NLTK.  
-  **Feature Extraction:** Uses **TF-IDF** to convert text into numerical vectors.  
-  **Model Training:** Trained using **KNeighborsClassifier** wrapped in a **OneVsRestClassifier**.  
-  **Evaluation:** Metrics such as accuracy, precision, recall, and F1-score ensure performance transparency.  
-  **Interactive Web App:** Built using **Streamlit** for instant, user-friendly predictions.

---

##  Model Performance

| Metric | Score |
|--------|-------|
| **Train Accuracy** | 0.9883 |
| **Test Accuracy** | 0.9845 |
| **Precision (avg)** | 0.98 |
| **Recall (avg)** | 0.97 |
| **F1-Score (avg)** | 0.97 |

✅ The model demonstrates excellent performance with minimal overfitting.

---

##  Technologies Used

- Python   
- Scikit-learn  
- NLTK  
- Pandas, NumPy  
- Streamlit  
- Pickle  

---

## 📊 Results Summary

- **Accuracy:** 98.45%  
- **Precision:** 0.98  
- **Recall:** 0.97  
- **F1-Score:** 0.97  

The confusion matrix has been saved as `confusion_matrix.png` for visualization.

---

## 🖥️ Access the Application

To run the app locally in Streamlit: ##http://localhost:8504/ 
