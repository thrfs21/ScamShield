
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC

# 1. Load dataset
df = pd.read_csv("fake_job_postings.csv")

text_columns = [
    "title",
    "company_profile",
    "description",
    "requirements",
    "benefits"
]

for col in text_columns:
    df[col] = df[col].fillna("").astype(str)

df["combined_text"] = df[text_columns].agg(" ".join, axis=1)
df = df.dropna(subset=["fraudulent"])

X = df["combined_text"]
y = df["fraudulent"].astype(int)

# 2. Split data consistently
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. Define five algorithms
algorithms = {
    "Multinomial Naive Bayes": MultinomialNB(),
    "Decision Tree": DecisionTreeClassifier(
        max_depth=30,
        class_weight="balanced",
        random_state=42
    ),
    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    ),
    "Linear SVM": LinearSVC(
        class_weight="balanced",
        random_state=42
    )
}

# 4. Train and evaluate every algorithm
results = []
trained_models = {}

for name, algorithm in algorithms.items():
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            max_features=30000,
            ngram_range=(1, 2),
            min_df=2,
            sublinear_tf=True
        )),
        ("classifier", algorithm)
    ])

    print(f"Training {name}...")
    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    scores = {
        "Algorithm": name,
        "Accuracy": accuracy_score(y_test, predictions),
        "Fraud Precision": precision_score(
            y_test, predictions, zero_division=0
        ),
        "Fraud Recall": recall_score(
            y_test, predictions, zero_division=0
        ),
        "Fraud F1-score": f1_score(
            y_test, predictions, zero_division=0
        )
    }

    results.append(scores)
    trained_models[name] = pipeline

# 5. Compare results
results_df = pd.DataFrame(results).sort_values(
    by="Fraud F1-score",
    ascending=False
)

print("\nMODEL COMPARISON")
print(results_df.to_string(index=False))

# 6. Save the model with the highest fraud F1-score
best_name = results_df.iloc[0]["Algorithm"]
best_model = trained_models[best_name]

joblib.dump(best_model, "scamshield_model.joblib")

print(f"\nBest model: {best_name}")
print("Saved as scamshield_model.joblib")
