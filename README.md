# 🛡️ ScamShield
### Machine Learning-Based Internship & Job Fraud Detection

ScamShield is a machine learning-based web application designed to identify potentially fraudulent job and internship postings. It analyses listing text and highlights suspicious indicators to help users make more informed decisions before applying.

## 🚀 Features

- **Fraud Prediction:** Classifies job postings using a trained machine learning model.
- **Risk Warning Indicators:** Highlights phrases related to upfront payments, guaranteed outcomes, and urgency.
- **Interactive Web Interface:** Simple interface built using Streamlit.
- **Multiple Input Fields:** Accepts job title, company profile, description, requirements, and benefits.
- **Safety Guidance:** Encourages users to independently verify employers before proceeding.

## 🧠 Machine Learning Approach

The project uses text-based machine learning to analyse job advertisements.

**Text preprocessing and feature extraction**
- Combines relevant text fields from job postings.
- Uses TF-IDF (Term Frequency–Inverse Document Frequency) to convert text into numerical features.
- Considers individual words and word pairs.

**Models explored**
- Multinomial Naive Bayes
- Decision Tree Classifier
- Logistic Regression

The models are evaluated using classification metrics, including precision, recall, F1-score, accuracy, and a confusion matrix.

The trained model is saved as `scamshield_model.joblib` and loaded by the Streamlit application.

## 📊 Dataset

The project uses the **Real or Fake: Fake Job Posting Prediction** dataset, commonly known as the Employment Scam Aegean Dataset (EMSCAD), available on Kaggle.

The dataset contains job postings labelled as fraudulent or legitimate.

Dataset source: [Fake Job Postings — Kaggle](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)

## 🛠️ Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- TF-IDF
- Streamlit
- Joblib
- Matplotlib

## 📁 Project Structure

```text
ScamShield/
├── app.py
├── requirements.txt
├── scamshield_model.joblib
├── README.md
├── screenshots/
│   └── app-demo.png
└── notebooks/
    └── model_training.ipynb
```

The `screenshots/` and `notebooks/` folders are optional additions. Create them only when you add the corresponding files.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/thrfs21/ScamShield.git
cd ScamShield
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL shown in your terminal, usually `http://localhost:8501`.

## 🧪 How to Use

1. Open the ScamShield web application.
2. Enter the job title and available company details.
3. Add the job description, requirements, and benefits.
4. Click **Analyse listing**.
5. Review the machine learning prediction and any warning indicators.
6. Independently verify the employer and job advertisement before taking action.

## 📈 Evaluation

The model is evaluated using a held-out test dataset and classification metrics.

Actual evaluation scores should be added here after training and testing the model.

| Metric | Result |
|---|---|
| Accuracy | Add measured result |
| Fraud Precision | Add measured result |
| Fraud Recall | Add measured result |
| Fraud F1-score | Add measured result |

## 🔮 Future Improvements

- Improve detection of suspicious wording and contextual patterns.
- Add model confidence or probability estimates where appropriately calibrated.
- Expand the dataset with newer job postings.
- Develop a more detailed explanation of the factors influencing predictions.
- Deploy the application online.

## ⚠️ Disclaimer

ScamShield is an educational machine learning project. Its predictions and text-based warning indicators are not proof that a job posting is fraudulent or legitimate. The application cannot independently verify employers, and users should confirm job offers through official company channels.

## 👨‍💻 Author

Developed as a Machine Learning Lab Assessment 2 project.
