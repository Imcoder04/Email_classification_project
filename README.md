# Spam Email Classifier

This project is a machine learning-based web app that classifies emails as **Spam** or **Not Spam** based on their content and metadata. The model is trained on the UCI Spambase dataset and deployed using Streamlit.

---

## Live Demo

🔗 [Click here to use the app](https://emailclassificationproject-huvuxauzcrzxssqfqd9ff2.streamlit.app/)

---

## Dataset

- **Source:** UCI Machine Learning Repository  
- **Dataset:** [Spambase Data Set](https://archive.ics.uci.edu/dataset/94/spambase)  
- **Features:** 57 attributes derived from email content (word frequencies, special character frequencies, etc.)

---

## Model Details

- **Algorithm:** Random Forest Classifier  
- **Preprocessing:** StandardScaler  
- **Training Platform:** Google Colab  
- **Export Format:** Pickle (`spam_rf_model.pkl`)

---

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python (scikit-learn, pandas, etc.)  
- **Deployment:** Streamlit Community Cloud  
- **Environment:** GitHub + VS Code


