# app.py

import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download NLTK resources (run once)
nltk.download('stopwords')
nltk.download('wordnet')

# ---------------------------------------------------
# 1️⃣ Text Cleaning Function
# ---------------------------------------------------
def cleaning_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = text.lower()
    words = text.split()
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

# ---------------------------------------------------
# 2️⃣ Load Pickle Files
# ---------------------------------------------------
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
clf = pickle.load(open('clf.pkl', 'rb'))

# ---------------------------------------------------
# 3️⃣ Category Mapping
# ---------------------------------------------------
category_mapping = {
    6:'Data Science',
    12: 'HR',
    0:'Advocate',
    1:'Arts',
    24:'Web Designing',
    16:'Mechanical Engineer',
    22:'Sales',
    14:'Health and fitness',
    5:'Civil Engineer',
    15:'Java Developer',
    4:'Business Analyst',
    21:'SAP Developer',
    2:'Automation Testing',
    11:'Electrical Engineering',
    18:'Operations Manager',
    20:'Python Developer',
    8:'DevOps Engineer',
    17:'Network Security Engineer',
    19:'PMO',
    7:'Database',
    13:'Hadoop',
    10:'ETL Developer',
    9:'DotNet Developer',
    3:'Blockchain',
    23:'Testing'
}

# ---------------------------------------------------
# 4️⃣ Streamlit UI Settings
# ---------------------------------------------------
st.set_page_config(page_title="Resume Classifier", page_icon="📄", layout="wide")
st.title("📄 Resume Screening System")
st.markdown("""
Welcome! Paste a resume below to predict the **job category**.  
This system uses **TF-IDF vectorization** and a **KNN classifier** trained on multiple categories.
""")

# Sidebar instructions
st.sidebar.header("Instructions")
st.sidebar.markdown("""
1. Paste the full resume text in the main panel.  
2. Click **Predict Category**.  
3. View the predicted category and ID.  
4. Make sure your text is in English.
""")

st.sidebar.header("About")
st.sidebar.info("This is a demo of a Resume Screening tool using TF-IDF + KNN.")

# ---------------------------------------------------
# 5️⃣ User Input Area
# ---------------------------------------------------
resume_text = st.text_area("📥 Enter Resume Text Here", height=300)

# Predict button in a centered layout
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Predict Category"):
        if resume_text.strip() == "":
            st.warning("⚠️ Please enter a resume text!")
        else:
            # Clean and vectorize
            cleaned_resume = cleaning_text(resume_text)
            inputs = tfidf.transform([cleaned_resume])
            prediction_id = clf.predict(inputs)[0]
            category_pred = category_mapping.get(prediction_id, 'unknown')
            
            # Display results with styling (black text)
            st.markdown("### ✅ Prediction Result")
            st.markdown(
                f"<div style='padding:20px; border-radius:10px; background-color:#DFF6FF; font-size:24px; text-align:center; color:black;'>{category_pred}</div>", 
                unsafe_allow_html=True
            )
            st.info(f"Prediction ID: {prediction_id}")
