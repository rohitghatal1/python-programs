import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

data = {
    "message": [
        "Congratulations! You won a free ticket to Bahamas, claim now!",
        "Hello, how are you doing today?",
        "Win $1000 cash by entering this contest!!!",
        "Are we still meeting for lunch?",
        "Free entry in a weekly prize draw, text WIN to 12345",
        "Hey, can you send me the notes from class?",
    ],
    "label": ["span", "ham", "spam", "ham", "spam", "ham"]
}

df = pd.DataFrame(data)


x = df["message"]
y = df["label"].map({"ham":0, "span": 1})

vectorizer = TfidfVectorizer(stop_words="english")
X_vec = vectorizer.fit_transform(x)


x_train, x_text, y_train, y_test = train_test_split(X_vec, y, test_size=0.3, random_state=42)


